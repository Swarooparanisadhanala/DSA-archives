class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        # Sort logs by their timestamp
        logs.sort(key=lambda item: item[1])

        # Attach original indices to queries so we can restore the original order later
        indexed_queries = sorted(
            enumerate(queries), key=lambda item: item[1]
        )

        ans = [0] * len(queries)
        active_servers = {}  # Map: server_id -> frequency in current window
        left = 0
        right = 0
        m = len(logs)

        for q_idx, q_val in indexed_queries:
            window_start = q_val - x
            window_end = q_val

            # Expand the sliding window's right bound up to window_end
            while right < m and logs[right][1] <= window_end:
                server_id = logs[right][0]
                active_servers[server_id] = (
                    active_servers.get(server_id, 0) + 1
                )
                right += 1

            # Shrink the sliding window's left bound from the left (remove logs older than window_start)
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1

            # Total servers (n) minus servers that received at least one request in the window
            ans[q_idx] = n - len(active_servers)

        return ans