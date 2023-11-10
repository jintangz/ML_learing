'''
Author: jinta jintangz@126.com
Date: 2023-03-19 13:52:24
LastEditors: jinta jintangz@126.com
LastEditTime: 2023-11-10 22:38:14
FilePath: \ML_learning\src\config.py
Description: 
Version: 
Copyright: kimzhao supported
'''



# 训练集路径
TRAIN_FILE = r'D:\CodeProject\financial_default\input\train.csv'

# 测试集路径
TEST_FILE = r'D:\CodeProject\financial_default\input\testA.csv'

# 目标变量列名
TARGET_NAME = 'isDefault'

# 训练集划分k折后的数据集
TRAIN_KFOLDS_FILE = r'D:\CodeProject\financial_default\input\train_kolds.csv'

# pandas_profile网页文件
REPORT_FILE = r'D:\CodeProject\financial_default\notebooks\report.html'



CATEGORY_FEATURE_MAP = {
'grade':'贷款等级',
'subGrade':'贷款等级之子级',
'employmentTitle':'就业职称',
'employmentLength':'就业年限（年）',
'homeOwnership':'借款人在登记时提供的房屋所有权状况',
'verificationStatus':'验证状态',
'issueDate':'贷款发放的月份',
'purpose':'借款人在贷款申请时的贷款用途类别',
'postCode':'借款人在贷款申请中提供的邮政编码的前3位数字',
'regionCode':'地区编码',
'initialListStatus':'贷款的初始列表状态',
'applicationType':'表明贷款是个人申请还是与两个共同借款人的联合申请',
'earliesCreditLine':'借款人最早报告的信用额度开立的月份',
'title':'借款人提供的贷款名称',
# 'policyCode':'公开可用的策略_代码=1新产品不公开可用的策略_代码=2',
}

# 离散数值特征
DISCRETE_FEATURE_MAP = {
'term':'贷款期限（year）',
'delinquency_2years':'借款人过去2年信用档案中逾期30天以上的违约事件数',
'openAcc':'借款人信用档案中未结信用额度的数量',
'pubRec':'贬损公共记录的数量',
'pubRecBankruptcies':'公开记录清除的数量',
'n0':'贷款人行为计数特征',
'n1':'贷款人行为计数特征',
'n2':'贷款人行为计数特征',
'n3':'贷款人行为计数特征',
'n4':'贷款人行为计数特征',
'n5':'贷款人行为计数特征',
'n6':'贷款人行为计数特征',
'n7':'贷款人行为计数特征',
'n8':'贷款人行为计数特征',
'n9':'贷款人行为计数特征',
'n10':'贷款人行为计数特征',
'n11':'贷款人行为计数特征',
'n12':'贷款人行为计数特征',
'n13':'贷款人行为计数特征',
'n14':'贷款人行为计数特征'
}

# 连续数值特征
CONTINUE_FEATURE_MAP = {
'loanAmnt':'贷款金额',
'interestRate':'贷款利率',
'installment':'分期付款金额',
'annualIncome':'年收入',
'dti':'债务收入比',
'revolBal':'信贷周转余额合计',
'revolUtil':'循环额度利用率，或借款人使用的相对于所有可用循环信贷的信贷金额',
'totalAcc':'借款人信用档案中当前的信用额度总数',
'ficoRangeLow':'借款人在贷款发放时的fico所属的下限范围',
'ficoRangeHigh':'借款人在贷款发放时的fico所属的上限范围'
}

