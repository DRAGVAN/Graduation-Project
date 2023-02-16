#include "UserWindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    UserWindow w;
    w.show();

    return a.exec();
}
