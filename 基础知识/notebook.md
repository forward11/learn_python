## chapter 3&4  列表
1. sort()是永久排序
   sorted()是临时排序
2. len()获长度
3. 数字列表
   1. range(a,b)随机生成数字(不包括b),可加第三参指定步长
   2. range()作为list()的参数
   3. 列表解析
        ```python
        squares=[value**2 for value in range(1,11)]
        ```
4. 1. 使用列表的一部分(切片)
    2. 复制列表 [:]
5. 元组(不可变的列表)
   1. 使用()表示元组
   2. 不可改变元组的值
   3. 可以给元组变量重新赋值

## chapter 5  if语句
1. 多条件用and和or
2. in判断元素是否在列表中
   not in
3. if-elif-else


## chapter 6  字典
1. 字典是一系列的键-值对
2. 字典是用{}定义
3. del 删除键值对
4. items()返回key-value列表
5. keys()只返回key
6. 遍历列表默认只遍历所有的key
7. sorted()来按照顺序遍历字典
8. values()遍历字典中的value
9. set()用于剔除重复值


## chapter 7  用户输入与while
1. for循环遍历列表是不能改变，使用while时可以继续修改

## chapter 8  函数
1. 传递实参
   1. 位置实参
   2. 关键字实参
2. 传递列表
   函数对列表的修改是永久性的，若要保留原列表，使用list[:]传递副本
3. 传递任意数量参
   1. (*toppings) 星号创建了一个元组
   2. (**user_info) 可接收任意数量的键值对，两个星号创建了一个空字典
4. 将函数存储在模块中
   1. 导入整个模块 
      1. 导入时 import 模块名
      2. 使用时 module.function()
   2. 导入特定的函数
   3. ``` python
      form module import function_1,function_2
      ```
   4. 使用as给函数指定别名
      ```python
      form module import function as fun
      ```
   5. 使用as给模块指定别名
      ```python
      import module as md
      ```
   6. 导入模块中的所有函数(几乎不用)
      ```python
      from module import *
      ```


## chapter 9  类
1. 创建类
   1. __init__()方法，会自动运行
      __init__()中的形参self不可少
   2. 可通过实例访问的变量称为属性
2. 使用类
   修改属性的值：
   1. 直接通过实例修改
   2. 通过方法设置
3. 继承
   1. 创建子类时父类必须在当前文件
   2. 在括号内指定子类名称
4. Python标准库
   ```python
   random.randint()返回一个位于指定范围内的整数
   ```

## chapter 10  文件和异常
1. open()函数用来打开文件
2. 关键字with在不再需要访问文件后将其自动关闭 
   ```python
   with open(...) as ... 
   ```
3. 全部读取 
   ```python
   read(file_object)
   ```
4. 逐行读取
   ```python
   for line in file_object:
      print(line)
   ```
5. 使用with时，open()返回的文件对象只在with代码块内使用，要在with块外使用时，将文件各行存储在一个列表中
   ```python
   with open(file_name) as file_object:
      lines=file_object.readlines()
   for line in lines:
      print(line)
   ```
6. 写入文件
   ```python
   with open(filename,'w) as file_object:
      file_object.write("I love Python")
   'w'是告诉python要以写入模式打开文件
   ```
   1. 'r' 读取模式
   2. 'w' 写入模式(清空旧数据)
   3. 'a' 附加模式(不清空旧数据)
   4. 'r+' 读加写
   5. 只能将字符串写入文本中
7. 异常
   1. try-except代码块处理异常
   2. 常见异常
   3. ```python
      ZeroDivisionError
      FileNotFoundError
      ```
   4. 在except语句块中使用pass什么都不做
   5. ```python
      line.count('apple')
      ```
      统计特定单词出现了多少次
8. 存储数据
   1. json.dump(data,file)存储数据，存储的数据和python中的数据格式一样
   2. json.load(file)可读取数据+格式，这是程序间共享数据的方式
9. 重构
   将代码划分为一系列完成具体工作的函数


## chapter11  测试代码 
1. 测试函数
   unittest模块提供了代码测试工具
   ```python
   import unittest
   
   class NamesTestCase(unittest.TestCase):
      #方法必须test_打头，才能自动运行
      #方法名必须是描述性的
      def test_function(self):  
         re=function()
         self.assertEqual(re,'right')
   
   unittest.main()   #让python运行测试代码
   ```
2. 测试类
   1. 每测试类的一个方法都有创建一个类的对象
   2. 使用setUp()方法，只需创建对象一次。因为，python会先执行setUp()，在运行以test_打头的方法。
   ```python
   class TestAnonymousSurvey(unittest.TestCase):
      def setUp(self):    
         question="what language did you first learn to speak?"
         self.my_survey=AnonymousSurvey(question)
         self.responses= ['english','chinese','spanish']

      def  test_store_single_response(self): 
         self.my_survey.store_response(self.responses[0])
         self.assertIn(self.responses[0],self.my_survey.responses)

      def test_store_three_response(self):
         for response in self.responses:
            self.my_survey.store_response(response)

         for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
            
   unittest.main()
   ```
   3. 可以在setUp()中创建一系列实例，并设置他们的属性

      
