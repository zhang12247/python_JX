from faker import Faker

if __name__ == '__main__':
    for i in range(1,1000):
        fake = Faker("zh_CN")
        print(fake.ssn(min_age=22, max_age=55))