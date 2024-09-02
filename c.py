import contextlib

items = ['apple', 'banana', 'orange']

# 存在しない 'grape' を削除しようとしてもエラーを無視する
with contextlib.suppress(ValueError):
    items.remove('grape')

print(items)  # ['apple', 'banana', 'orange']