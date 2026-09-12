class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit):
            visit.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visit)

        # Pacific: top and left
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: bottom and right
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        return list(pacific & atlantic)