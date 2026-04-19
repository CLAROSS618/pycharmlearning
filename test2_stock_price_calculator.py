name = "哥伦比亚矿业公司"
stock_price = 100
stock_code = 104
stock_price_daily_growth_factor = 1.12
growth_days = 7
price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{price}")
print("每日增长系数是：%.2f,经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, price))
