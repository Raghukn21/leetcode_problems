class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self._is_valid_ipv4(queryIP):
            return "IPv4"
        if self._is_valid_ipv6(queryIP):
            return "IPv6"
        return "Neither"

    def _is_valid_ipv4(self, ip: str) -> bool:
        parts = ip.split('.')

        # Must have exactly 4 parts — using split('.') on "1.2.3.4." gives 5 parts
        # (the trailing dot creates an empty string at the end), catching that edge case
        if len(parts) != 4:
            return False

        for part in parts:
            # Empty segment (e.g. from "1..2.3") or leading zero (e.g. "01")
            if not part:
                return False
            # Only digits allowed — no signs, spaces, or letters
            if not part.isdigit():
                return False
            # Leading zeros: "01", "00" etc. are invalid; "0" alone is fine
            if len(part) > 1 and part[0] == '0':
                return False
            # Value must be in [0, 255]
            if int(part) > 255:
                return False

        return True

    def _is_valid_ipv6(self, ip: str) -> bool:
        parts = ip.split(':')

        if len(parts) != 8:
            return False

        valid_hex_chars = set('0123456789abcdefABCDEF')

        for part in parts:
            # Each group must be 1 to 4 hex characters
            if not part or len(part) > 4:
                return False
            # All characters must be valid hex digits (leading zeros allowed)
            if not all(ch in valid_hex_chars for ch in part):
                return False

        return True