from googlesearch import search
import pandas as pd
from tqdm import tqdm


def google_search(query, n):
    i = 0
    while True:
        results = search(query, lang='en', stop=n + 5 * i)
        urls = []
        ans = []

        for j in results:
            if j.split(sep='/')[2] not in urls:
                ans.append(j)
            urls.append(j.split(sep='/')[2])

        if len(ans) >= n:
            return ans[:n]
        else:
            i = i + 1


if __name__ == '__main__':
    # path = input('Enter file path: ')
    path = 'test.xlsx'
    n_col = int(input('Enter numbers of columns to make query: '))
    n_res = int(input('Enter number of results: '))
    data = pd.read_excel(path, header=None)
    results = []
    for i in tqdm(range(data.shape[0])):
        query = ' '.join(data.iloc[i, :n_col].values)
        results.append(google_search(query, n_res))
    data = pd.concat([data, pd.DataFrame(results)], axis=1)
    data.to_excel('test.xlsx', header=False, index=False)
