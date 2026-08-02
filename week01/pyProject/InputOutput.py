hours_worked = 8;
hourly_pay_rate = 25.5;

if __name__ == "__main__":
  hours_worked = float(input("Please input Hours worked: "));
  hourly_pay_rate = float(input("Please input Hourly pay rate: "));

  gross_pay = hours_worked * hourly_pay_rate;
  print("Gross pay: $", gross_pay);