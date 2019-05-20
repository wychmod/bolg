def replace_red(str, con):
    if str:
        str = str.replace(con, '<span style="color:red;">' + con + '</span>')
    return str

print(replace_red('我是一只小小鸟','是'))