import os
import cv2 as cv
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

background_dir = os.listdir('task2img/backgroundimg/')
pores_dir = os.listdir('task2img/poresimg/')


def build_dataset():
    """ Build data set for training and testing (select first 2500 images of each directory)
    Args:
        temp_img: a temporary list to store all pixels of an image
        set_img: a list including all images used to build a DataFrame
        background: a DataFrame storing data of background info
        pores: a DataFrame storing data of pores info
        dataset: a labeled dataset including background and pores
    Returns:
        dataset_x: the data of the dataset
        dataset_y: the label of the dataset
    Raises:
        not defined
    """
    set_img = []
    temp_img = []
    for i in range(len(background_dir)):
        img = cv.imread('task2img/backgroundimg/' + background_dir[i], 0)
        for rows in img:
            for pixel in rows:
                temp_img.append(pixel)
        set_img.append(temp_img)
        temp_img = []
    background = pd.DataFrame(data=set_img)
    background['label'] = 0

    set_img = []
    temp_img = []
    for i in range(len(pores_dir)):
        img = cv.imread('task2img/poresimg/' + pores_dir[i], 0)
        for rows in img:
            for pixel in rows:
                temp_img.append(pixel)
        set_img.append(temp_img)
        temp_img = []
    pores = pd.DataFrame(data=set_img)
    pores['label'] = 1

    dataset = background.append(pores, ignore_index=True)
    dataset_x = dataset.drop(columns='label', axis=1)
    dataset_y = dataset['label']

    return dataset_x, dataset_y


def train_svm(x, y):
    """ train and test data using SVM
        Args:
            x_train: training data
            x_test: testing data
            y_train: label of training data
            y_test: label of testing data
            ss: standard scaler from sklearn.preprocessing
            clf: LinearSVC from sklearn.svm
        Returns:
            not defined
        Raises:
            not defined
        """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)
    clf = LinearSVC(C=1.5, tol=0.00001, loss='hinge', max_iter=2000)
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)

    print(classification_report(y_test, y_predict))


def main():
    x, y = build_dataset()
    train_svm(x, y)


if __name__ == '__main__':
    main()
