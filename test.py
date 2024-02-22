import threading

# 使用RLock
lock = threading.RLock()

def recursive_function(count):
    if count > 0:
        with lock:  # with代码执行完。锁就释放了
            print(f"获取锁，当前计数：{count}")
            recursive_function(count - 1)
    print(f"释放锁，当前计数：{count}")  # 这行代码在退出with语句块时隐式发生

# 尝试使用Lock，看看会发生什么
# lock = threading.Lock()

def main():
    recursive_function(5)

if __name__ == "__main__":
    main()
