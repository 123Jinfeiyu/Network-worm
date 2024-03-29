from pyspark.sql import SparkSession
import os

url = "jdbc:mysql://localhost:3306/jiuzaigou?useUnicode=true&useSSL=false&characterEncoding=utf-8"
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars mysql-connector-java-5.1.47.jar pyspark-shell'
spark = SparkSession. \
    Builder(). \
    appName('sql'). \
    master('local'). \
    getOrCreate()
# 读取数据集为DataFrame
df = spark.read.format('com.databricks.spark.csv').options(header='false').load('jiuzhaigou.csv') \
    .toDF("username", "usertype", "score", "zan", "sc", "times", "comment")
print(df)
df.createOrReplaceTempView("jiuzaigou")


# 1 数据入库
def step01():
    step1 = spark.sql("select * from jiuzaigou")
    step1.show()
    step1.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='jiuzaigou',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


# 2 每天评论数量
def step02():
    step2 = spark.sql("select substring (times,0,10) as day, count(*) as num from jiuzaigou group by day order by day asc")
    step2.show()
    step2.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='day',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


# 3 不同长叶云杉占比
def step03():
    step3 = spark.sql("select usertype,count(*) as num from jiuzaigou group by usertype")
    step3.show()
    step3.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='usertype',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


# 4 优秀评论
def step04():
    step4 = spark.sql("select username,zan,comment from jiuzaigou order by zan desc limit 30")
    step4.show()
    step4.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='good',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


# 5 评分分布
def step05():
    step05 = spark.sql("select score,count(*) as num from jiuzaigou group by score")
    step05.show()
    step05.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='score',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


# 6 每小时发布评论
def step06():
    step06 = spark.sql(
        "select substring (times,12,2) as hour, count(*) as num from jiuzaigou group by hour order by hour asc")
    step06.show()
    step06.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='hour',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


if __name__ == "__main__":
    # step01()
    step02()
    step03()
    step04()
    step05()
    step06()
    spark.stop()
