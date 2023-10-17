import sqlglot
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.qualify_tables import qualify_tables

def main(sql_query, read, write, method):
    if method == 1:
        # with open("all-test-case-smartbi2.sql", "r") as input_file:
        #     sql = input_file.read()
        result = sqlglot.transpile(sql_query, read=read, write=write, pretty=True)[0]
        # 将结果写入文件
        # with open("res.sql", "w") as file:
        #     for item in result:
        #         file.write("%s;\n" % item)
        print(result)
    elif method == 2:#当有别名不全或者表名大小写需要更改，可以将method设置为2

        res = sqlglot.transpile(sql_query, read=read, write=write, pretty=True)[0]
        expression = sqlglot.parse_one(res, read=read)
        # True 代表将表名改为大写，False 代表将表名改成小写，None 代表不改变表名大小写，默认值为None
        result = qualify_tables(expression, case_sensitive=False).sql()
        print(result)
    elif method == 3:#当有别名(列名)语法时，可以将method设置为3，进行改写
        # 改写列别名
        expression = sqlglot.parse_one(sql_query)
        print(qualify(expression, quote_identifiers=False).sql())
    else:
        print("Invalid method specified.")

sql = """
select array_to_string(array[1,2,3,4,NULL,6], ',');
"""

# 使用参数值调用 main 函数，传入相应的参数
# main(sql, "snowflake", "doris", 1)
main(sql, "postgres", "doris", 1)
# main(sql, "snowflake", "doris", 3)