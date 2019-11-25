import sqlite3
import random


source = 'qwertyhnbgfvcds86xzaujmikolp'


# 生成字符串的函数
def get_str(x, y):
    str_num = random.randint(x, y)
    astr = ''
    for i in range(str_num):
        astr += random.choice(source)

    return astr


# 生成一个数据列表的函数
def get_data_list(n):
    lists = []
    for i in range(n):
        lists.append((get_str(2, 4), get_str(8, 12)))

    return lists


def output():
    cur.execute('SELECT * FROM t_person')
    for sid, name, ps in cur:
        print(sid, ' ', name, ' ', ps)


def output_all():
    cur.execute('SELECT * FROM t_person')
    for item in cur.fetchall():
        print(item)


if __name__ == '__main__':
    con = sqlite3.connect(':memory:')
    cur = con.cursor()

#   创建一个表
    cur.execute('CREATE TABLE t_person('
                'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                'name TEXT, '
                'password TEXT)')

#   向表中添加数据
    cur.execute('INSERT INTO t_person '
                '(name, password) '
                'VALUES '
                '(?, ?)', (get_str(2, 4), get_str(8, 12)))
    output()

#   在表中添加多条数据
    cur.executemany('INSERT INTO t_person (name, password) VALUES (?, ?)', get_data_list(3))
    output_all()


#   删除某条数据
    cur.execute('DELETE FROM t_person WHERE id = ?', (3,))
    output()

    cur.close()
