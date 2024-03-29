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
df = spark.read.format('com.databricks.spark.csv').options(header='true').load('NLP测试后数据.csv')
df.createOrReplaceTempView("jiuzaigou")


# 1 评论情感分析统计
def step01():
    step1 = spark.sql("select sent,count(*) as num from jiuzaigou group by sent")
    step1.show()
    step1.write.mode('overwrite').format("jdbc").options(
        url=url,  # 开启批处理
        driver="com.mysql.jdbc.Driver",
        user='root',
        password='123456',
        dbtable='sent',
        batchsize=10000,  # 每批数据大小
        isolationLevel='NONE',  # 事务隔离,这里不需要做事务隔离
        truncate='true'  # 如果不加次参数，overwrite则是删除表重新创建，加上则时trunacte 表而不删除
    ).save()


if __name__ == "__main__":
    step01()
    spark.stop()
