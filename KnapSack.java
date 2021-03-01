public class KnapSack {
public static int knapsack(int[] values, int[] weights, int sum){

        int n = weights.length;

        int[][] dp = new int[n+1][sum+1];

        for(int i = 0; i < n; i++) {
                dp[0][i] = 0;
        }


        for(int i = 1; i <=n; i++) {
                for(int j = 1; j <= sum; j++) {
                        if(weights[i-1] <= j) {
                                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1]);
                        }

                }

        }
        return dp[n][sum];

}

public static void main(String[] args){

        int[] values = {60, 100, 120};
        int[] weights = {10, 20, 30};
        int capacity = 50;

        System.out.println(knapsack(values, weights, capacity));
}


}
