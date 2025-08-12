class ApogeeDetector:
    """
    Detects when apogee (peak altitude) is reached.
    Simple algorithm: If altitude starts decreasing for N consecutive samples, trigger ejection.
    """

    def __init__(self, consecutive_drops=3):
        self.consecutive_drops = consecutive_drops
        self.prev_altitude = None
        self.drop_count = 0
        self.triggered = False

    def update(self, t, altitude):
        """
        Update detector with a new telemetry point.
        Returns True if ejection should occur.
        """
        if self.triggered:
            return False  # already triggered

        if self.prev_altitude is not None:
            if altitude < self.prev_altitude:
                self.drop_count += 1
            else:
                self.drop_count = 0

            if self.drop_count >= self.consecutive_drops:
                self.triggered = True
                print(f"[ApogeeDetector] Apogee detected at t={t:.2f}s, alt={self.prev_altitude:.2f} m")
                return True

        self.prev_altitude = altitude
        return False
