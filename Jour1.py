import pandas as pd

# df = pd.read_csv("Puzzles\\Historian hysteria_test.txt", sep=r'\s+', header=None)
df = pd.read_csv("Puzzles\\Historian hysteria.txt", sep=r'\s+', header=None)


# PART I ################################################


df_sorted = df.apply(lambda x: x.sort_values().values)
df_sorted["diff"] = abs(df_sorted[0] - df_sorted[1])
result_1 = df_sorted['diff'].sum()

print('The total distance between left and right lists is', result_1)


# PART II ################################################


result_2 = 0

for nb_left in df[0]:
    count = 0
    for nb_right in df[1]:
        if nb_left == nb_right:
            count += 1
    result_2 += nb_left * count


# Another PART II ################################################

counts_col_1 = df[1].value_counts()
counts_col_0_in_col_1 = df[0].map(counts_col_1)
result_2_bis = (df[0] * counts_col_0_in_col_1).sum()

print('The similarity score is', round(result_2_bis))