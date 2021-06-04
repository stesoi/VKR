import pandas as pd
import os
import bagpy as bp
import rosbag
import rospy
import subprocess
import yaml
import csv


if __name__ == '__main__':
    file = 'test.bag'
    # print(os.path.exists(path=path))
    # print(os.path.isfile(path=path))

    # Через библиотеку bagpy
    # Лучший вариант чтения и записи

    if(os.path.exists(path=file) and os.path.isfile(path=file)):
        # метаданные
        b = bp.bagreader(bagfile=file)
        print(b.topic_table)

        # разделение информации по топикам и запись в csv файлы
        csv_files = []
        for t in b.topics:
            data = b.message_by_topic(t)
            csv_files.append(data)
        print(csv_files)

        # построение графика одометрии
        b.plot_odometry()



    # Через библиотеку rosbag

    # Получение информации
    # info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', file], stdout=subprocess.PIPE).communicate()[0])

    # info_dict = yaml.load(rosbag.Bag(file, 'r')._get_yaml_info())
    # print(info_dict)

    # bag = rosbag.Bag('test.bag')
    # topics = bag.get_type_and_topic_info()[1].keys()
    # types = []
    # for i in range(0, len(bag.get_type_and_topic_info()[1].values())):
    #     types.append(bag.get_type_and_topic_info()[1].values()[i][0])

    # Преобразование в CSV файл
    # bag = rosbag.Bag(file)
    # results_dir = "results"
    # if not os.path.exists(results_dir): # создание директории
    #     os.makedirs(results_dir)
    # with open(results_dir + "/" + file[:-4] + '_joint_states.csv', mode='w') as data_file:
    #     data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # # получение сообщений по топикам
    # for topic, msg, t in bag.read_messages(topics=['/joint_states']):
    #     if msg.name[0] == "robot_elbow_joint":
    #         p = msg.position
    #         data_writer.writerow([t, p[0], p[1], p[2], p[3], p[4], p[5]])
    # bag.close()



    # Еще вариант с библиотекой bagpy
    # https://github.com/jmscslgroup/bagpy/blob/master/notebook/bagpy_example.py

    # b = bp.bagreader(file)

    # # Read Laser Data
    # csv = b.laser_data()
    # df = pd.read_csv(csv[0])

    # # Read Velocity Data
    # ms = b.vel_data()
    # vel = pd.read_csv(ms[0])

    # # Read Standard Messages
    # s = b.std_data()
    # data = pd.read_csv(s[0])

    # # Read odometry Data
    # odom = b.odometry_data()
    # odomdata = pd.read_csv(odom[0])

    # # Read Wrench Data
    # w = b.wrench_data()
    # wdata = pd.read_csv(w[0])

    # # Get the plots
    # b.plot_odometry()
    # b.plot_vel()
    # b.plot_wrench()
    # # Animate Velocity Timeseries
    # bagpy.animate_timeseries(vel['Time'], vel['linear.x'], title='Velocity Timeseries Plot')

