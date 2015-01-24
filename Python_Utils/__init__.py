#-*- coding: utf-8 -*-
# __init__.py


def save_data(filename, data):
    """Save data as pkl file"""
    import gzip
    import pickle
    import cPickle
    if filename.endswith('.pkl.gz'):
        f = gzip.open(filename, 'wb')
    elif filename.endswith('.pkl'):
        f = open(filename, 'wb')
    else:
        raise ValueError('filename should end with .pkl or .pkl.gz')

    try:
        cPickle.dump(data, f)
    except MemoryError:
        pickle.dump(data, f)
    f.close()


def load_data(filename):
    """Load data from pkl file"""
    import gzip
    import pickle
    import cPickle
    if filename.endswith('.pkl.gz'):
        f = gzip.open(filename, 'rb')
    elif filename.endswith('.pkl'):
        f = open(filename, 'rb')
    else:
        raise ValueError('filename should end with .pkl or .pkl.gz')

    try:
        data = cPickle.load(f)
    except MemoryError:
        data = pickle.load(f)
    f.close()

    return data


def save_tocsv(filename, data, header=None):
    """Save data to csv"""
    import csv
    # data initialization
    n_col = len(data[0])
    if header is None:
        header = ['col{}'.format(i) for i in range(n_col)]
    elif len(header) != n_col:
        raise ValueError('number of header & data cols should be same')

    f = open(filename, 'wb')
    writer = csv.writer(f)

    # write to csv
    writer.writerow(header)
    for row in data:
        if len(row) != n_col:
            raise ValueError('number of data cols should be const')
        writer.writerow(row)

    f.close()


def connect_db(db, host='localhost', user='root',
               passwd='', charset='utf8'):
    """Connect to the database"""
    import MySQLdb
    con = MySQLdb.connect(db=db, host=host, user=user,
                          passwd=passwd, charset=charset)
    return con


def get_db_data(sql, db, host='localhost', user='root', passwd=''):
    """Get DB data by given SQL"""
    import pandas.io.sql as psql
    con = connect_db(db=db, host=host, user=user, passwd=passwd)
    db_data = psql.read_sql(sql, con)
    con.close()
    return db_data


def get_filename_frompath(path):
    filename = path.split('/')[-1]
    return filename


def change_filename(filename, extension):
    changed = ''.join(filename.split('.')[:-1]) + extension
    return changed


def plot_3D(X, Y, Z, color='b', marker='o',
            xlim=None, ylim=None, zlim=None,
            alpha=0.5, savefig=None, show=True):
    """Plot 3 dimension arrays"""
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)

    # Setting the axes properties
    if xlim is None:
        ax.set_xlim3d([X.min(), X.max()])
    elif len(xlim) == 2:
        ax.set_xlim3d(xlim)
    ax.set_xlabel('X')
    if ylim is None:
        ax.set_ylim3d([Y.min(), Y.max()])
    elif len(ylim) == 2:
        ax.set_ylim3d(ylim)
    ax.set_ylabel('Y')
    if zlim is None:
        ax.set_zlim3d([Z.min(), Z.max()])
    elif len(zlim) == 2:
        ax.set_zlim3d(zlim)
    ax.set_zlabel('Z')
    ax.set_title('3D plot')

    ax.view_init(-10, 30)
    ax.scatter(X, Y, Z, c=color, marker=marker, alpha=alpha)
    # ax.plot(X, Y, Z, c=color, alpha=alpha)

    if type(savefig) == str:
        plt.savefig(savefig)

    if show is True:
        plt.show()

    plt.clf()
    plt.close()


def plot_3D_animation(X, Y, Z, n_frame=None,
                      xlim=None, ylim=None, zlim=None,
                      step=None, saveanime=None, show=True):
    """3D plotting animation"""
    import numpy
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import mpl_toolkits.mplot3d.axes3d as p3
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    if step is None:
        step = 1
    X = X[range(0, len(X), step)]
    Y = Y[range(0, len(Y), step)]
    Z = Z[range(0, len(Z), step)]

    data = [numpy.vstack((X, Y, Z))]

    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1],
                     dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    if xlim is None:
        ax.set_xlim3d([X.min(), X.max()])
    elif len(xlim) == 2:
        ax.set_xlim3d(xlim)
    ax.set_xlabel('X')
    if ylim is None:
        ax.set_ylim3d([Y.min(), Y.max()])
    elif len(ylim) == 2:
        ax.set_ylim3d(ylim)
    ax.set_ylabel('Y')
    if zlim is None:
        ax.set_zlim3d([Z.min(), Z.max()])
    elif len(zlim) == 2:
        ax.set_zlim3d(zlim)
    ax.set_zlabel('Z')
    ax.set_title('3D animation')
    ax.view_init(-10, 30)

    def update_lines(num, dataLines, lines):
        for line, data in zip(lines, dataLines):
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2,:num])
        return lines

    if n_frame is None:
        n_frame = len(X)

    # Creating the Animation object
    anim = animation.FuncAnimation(fig,
                                   update_lines,
                                   n_frame,
                                   fargs=(data, lines),
                                   interval=1,
                                   blit=False)

    if type(saveanime) == str:
        writer = animation.FFMpegWriter()
        anim.save(saveanime, writer=writer)

    if show is True:
        plt.show()

    plt.clf()
    plt.close()


def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    import cv2
    # Capture camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Act like mirror or not
        if mirror is True:
            frame = frame[:,::-1]

        # Resize frame
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        # Display the resulting frame
        cv2.imshow('camera capture', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('capture.png', frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def play_video(video_name):
    """Play avi video"""
    import cv2
    cap = cv2.VideoCapture(video_name)

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('video', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('video_frame.png', frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
