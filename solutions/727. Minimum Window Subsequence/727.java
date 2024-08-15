class Solution {
  public String minWindow(String s1, String s2) {
    final int m = s2.length();
    final int n = s1.length();
    // dp[i][j] := the start index (1-indexed) of the minimum window of s2[0..i)
    // and s1[0..j).
    int[][] dp = new int[m + 1][n + 1];

    // Fill in the placeholder values.
    for (int j = 0; j <= n; ++j)
      dp[0][j] = j + 1;

    for (int i = 1; i <= m; ++i)
      for (int j = 1; j <= n; ++j)
        if (s2.charAt(i - 1) == s1.charAt(j - 1))
          dp[i][j] = dp[i - 1][j - 1];
        else
          dp[i][j] = dp[i][j - 1];

    int bestLeft = 0;
    int minLength = Integer.MAX_VALUE;

    for (int j = 1; j <= n; ++j)
      if (dp[m][j] > 0 && j - dp[m][j] + 1 < minLength) {
        bestLeft = dp[m][j] - 1;
        minLength = j - dp[m][j] + 1;
      }

    return minLength == Integer.MAX_VALUE ? "" : s1.substring(bestLeft, bestLeft + minLength);
  }
}
