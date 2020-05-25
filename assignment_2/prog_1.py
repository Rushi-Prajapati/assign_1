class personal_info:
  def __init__(self):
    print('personal_info created.')

  def __del__(self):
    print('personal_info deleted.')

personal_info1 = personal_info()
del personal_info1