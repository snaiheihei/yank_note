# thread

::: tip GIL
- GIL全局解释器锁： 全局锁的存在会对多线程的效率有不小影响。甚至就几乎等于Python是个单线程的程序； 
- 多线程会争取一个python解释器，会被分配时间片去执行解释各自的代码；
- python的多线程一个主要用途就是==异步==分配任务执行；
- 验证单线程多线程多进程对多核心cpu的使用情况：
    linux ==htop 实时查看多核使用情况==
    脚本模拟单线程，多线程，多进程（在linux系统中执行）
   ```python
    import threading
    import multiprocessing

    print(__file__)
    def run():
        while True:
            pass
    # threading.Thread(target=run).start() # 多线程，多线程获取锁资源，多核不能并行处理
    # multiprocessing.Process(target=run).start() # 多进程，多核并行
    # 默认单线程，单核使用
    while True:
        pass
   ```
   shell中模拟多核高负载
   ```bash
   time echo "scale=20000;4*a(1)" | bc -lq &
   time echo "scale=20000;4*a(1)" | bc -lq &
   ```
   go goroutine协程可以并行完整利用多核CPU
  ```go
    package main

    func subprocess(){
            for{}
            }

    func main(){
            // 开启一go协程
            go subprocess()
            for{}
            }
  ```
  
:::

::: tip 多线程
- 创建对象时，代表 Thread 内部被初始化。调用 start() 方法后，thread 会开始运行。thread 代码正常运行结束或者是遇到异常，线程会终止。
- join() 方法的功能是在程序指定位置，优先让该方法的调用者使用CPU资源.t1 t2线程都会阻塞主线程；
- 异步操作时，不阻塞主进程循环时不要加入join(),如web API时。
- 守护线程，是为守护别人而存在，当设置为守护线程后，被守护的主线程不存在后，守护线程也自然不存在。
- Python多线程的默认情况（设置线程setDaemon(False)），主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。
```python
import threading
import time

def test(num):
    for i in range(num):
        print(threading.currentThread().name)
        time.sleep(0.8)

# 每一个 Thread 都有一个 name 的属性，默认就是 “Thread-N” 的形式，N 是数字
# daemon=True 常用于异步线程（不加join()),守护主线程，主线程结束立即结束
t1 = threading.Thread(target=test, args=(5,), daemon=True)
t2 = threading.Thread(target=test, args=(5,), daemon=True)
t1.start()
t2.start()
# t1 t2会优先获取cpu资源，阻塞主线程
t1.join()
t2.join()

for i in range(11, 16):
    print(threading.currentThread().name)
    time.sleep(0.2)
```

:::
::: tip 互斥锁
- threading模块里面有lock类，可以创建一把锁，在执行到关键代码处，加锁，在这把锁没有释放之前，不会切换其他线程，这就解决了前面的多线程共享全局变量问题。
- RLock递归锁
   ```python
    a = 0
    lock = threading.Lock() #创建一把锁
    def func1():
        global a
        for i in range(1000000):
            lock.acquire() #修改前加一把锁
            a += 1
            lock.release() #修改完释放锁
        print(a)

    def func2():
        global a
        for i in range(1000000):
            lock.acquire() # 修改前加一把锁
            a += 1
            lock.release() # 修改完释放锁
        print(a)

    th1 = threading.Thread(target=func1)  
    th2 = threading.Thread(target=func2)  
    th1.start()  #启动线程1
    th2.start()  #启动线程2
    th1.join()   #在子线程1完成运行之前，主线程将一直等待
    th2.join()   #在子线程2完成运行之前，主线程将一直等待
    #输出-------------------------------------
    1808484
    2000000

   ```
   
:::


