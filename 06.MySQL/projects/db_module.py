import pymysql
# 월별 매출/이익
def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = '''
    SELECT DATE_FORMAT(sdate, '%m') AS `month`,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
    FROM sales_book
    GROUP BY `month`
    ORDER BY `month`;
    '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
# 거래처별 매출/이익
def get_data_by_company(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = '''
    SELECT scompany,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
    FROM sales_book
    GROUP BY scompany
    ORDER BY revenue DESC;
    '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
# 거래처별 판매제품/수량
def get_products_by_company(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = '''
    SELECT scompany, pname,
    SUM(sunit) AS unit
    FROM sales_book
    GROUP BY scompany, pname
    ORDER BY scompany;
    '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
# 제품별 판매수량/매출/이익
def get_data_by_products(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = '''
    SELECT pname,
    SUM(sunit) AS unit,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
    FROM sales_book
    GROUP BY pid
    ORDER BY pid;
    '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
# 카테고리별 매출/이익
def get_data_by_category(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = '''
    SELECT pcategory,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
    FROM sales_book
    GROUP BY pcategory;
    '''
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results