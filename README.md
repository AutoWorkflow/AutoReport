# SUT daily report   
沈阳工业大学每日健康上报，使用Github Actions自动完成。    
仅供交流学习，请不要谎报瞒报！    
# 使用说明  
## 配置Actions
### 1. fork到自己的仓库  

&nbsp;&nbsp;&nbsp;&nbsp;点击右上角的fork，完成后会自动跳转到你fork的仓库  
  
### 2. 设置用户名和密码  

&nbsp;&nbsp;&nbsp;&nbsp;点击Settings->Sectets->New Secrets，添加:    

| NAME     | VALUE  |
| -------- | -----  |  
| USERNAME | 用户名 |   
| PASSWORD | 密码   |   
| ADDRESS  | 打卡地点 |

打开地点的格式: *定位*<@>*详细地址*    
例：中国,辽宁省,沈阳市,铁西区<@>沈阳工业大学 

### 3. 测试配置
&nbsp;&nbsp;&nbsp;&nbsp;打开Actions，在Select workflow处选择daily deport，执行Run workflow，查看运行日志    
    
到这一步就已经可以自动运行了，如果想修改打卡的选项或每天自动打卡的时间请查看下面的**配置文件**部分

### 4. 如何取消自动运行    
删除.github/workflows/main.yml文件，    
或者在Setting->Action->选择Disable Actions for this repository。该仓库的工作流将不再运行

## 配置文件    
### 配置打卡数据
config.yml
配置需要改动的打卡数据(不需要改动的数据可以不填写)
```
jrcltw:    
  今日测量体温 注意：一定要加引号，不然会提交失败
mqszd:
  目前所在地：沈阳市/辽宁省非沈阳市/其他地区(非辽宁省)    
sfybh:    
  是否有变化：是/否
xcsj:
  行程时间：如果为空填写null
```
### 配置自动运行时间
每日任务执行的时间，由.github/workflows/report.yml 中的cron表达式指定，    
默认的执行时间为每日的11点和16点:
```
on:
  schedule:
    # UTC时间，UTC+8时间需要在原时间上减去8
    - cron:  '0 3,8 * * *'
```
## 本地运行
```
pip install -r requirements.txt
python report.py -u 用户名（学号） -p 密码
```
