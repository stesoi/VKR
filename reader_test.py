import pandas as pd
import os
import bagpy as bp


if __name__ == '__main__':
    path = 'test.bag'
    # print(os.path.exists(path=path))
    # print(os.path.isfile(path=path))

    if(os.path.exists(path=path) and os.path.isfile(path=path)):
        # метаданные
        b = bp.bagreader(bagfile=path)
        print(b.topic_table)

        # разделение информации по топикам и запись в csv файлы
        csv_files = []
        for t in b.topics:
            data = b.message_by_topic(t)
            csv_files.append(data)
        print(csv_files)

        # построение графика одометрии
        b.plot_odometry()


    # ниже код пример - https://github.com/jmscslgroup/bagpy/blob/master/notebook/bagpy_example.py
    # # Read Laser Data
    # csv = b.laser_data()
    # df = pd.read_csv(csv[0])
    #
    # # Read Velocity Data
    # ms = b.vel_data()
    # vel = pd.read_csv(ms[0])
    #
    # # Read Standard Messages
    # s = b.std_data()
    # data = pd.read_csv(s[0])
    #
    # # Read odometry Data
    # odom = b.odometry_data()
    # odomdata = pd.read_csv(odom[0])
    #
    # # Read Wrench Data
    # w = b.wrench_data()
    # wdata = pd.read_csv(w[0])
    #
    # # Get the plots
    # b.plot_odometry()
    # b.plot_vel()
    # b.plot_wrench()
    # # Animate Velocity Timeseries
    # bagpy.animate_timeseries(vel['Time'], vel['linear.x'], title='Velocity Timeseries Plot')