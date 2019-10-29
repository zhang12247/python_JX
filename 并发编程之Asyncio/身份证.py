from faker import Faker
import cProfile
import pdb
import linecache

if __name__ == "__main__":

    def genid():
        for i in range(1, 45000):
            # with open('C:\\Users\\zhangjiabin\\Desktop\\aa.txt') as ff:
            #     print(i)
            #     print(ff.readline(i))
            # print("{" + linecache.getline('C:\\Users\\zhangjiabin\\Desktop\\aa.txt', i))
            fake = Faker("zh_CN")
            # sqlString = "INSERT INTO `fin_datasupport_case` (`user_id`, `credit_apply_no`, `case_no`, `id_type`, `id_no`, `name`, `product_code`, `product_name`, `report_no`, `report_time`, `batch`, `warning_type`, `warning_result`, `distribution_type`, `check_status`, `need_scan`, `upload_end_time`, `period`, `remark`, `creator`, `gmt_created`, `modifier`, `gmt_modified`, `is_deleted`) VALUES ('{}', 'TTFXJ20190128000107135407401\r\nTTFXJ20190128000107135407401\r\n', '20190129c93f204f2a234512af83d79fb192af77', 'ID_CARD', '{}', '{}', 'za-themisTTFXJ', '放心借_za-themisTTFXJ', '2019012700006901330847', '2019-06-18 10:57:19', '20190129', 'SYSTEM', 'PASS', 'SYSTEM', 'PENDING', NULL, NULL, NULL, NULL, 'SYSTEM', '2019-06-12 10:58:04', 'SYSTEM', '2019-07-25 11:40:26', 'N')".format(
            #     fake.phone_number(), fake.ssn(), fake.name()
            # )
            # qq = '"caId":"{}"'.format(fake.phone_number())
            # print(qq+"}")
            print(fake.ssn())
            # print(fake.name())

    genid()
