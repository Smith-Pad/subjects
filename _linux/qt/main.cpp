/**
main.cpp
**/

#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QVBoxLayout>
#include <QWidget>
#include <QLabel>
#include <QDockWidget>

class MainWindow : public QMainWindow {
public:
    MainWindow() {
        // Create central widget and set layout
        auto centralWidget = new QWidget;
        auto layout = new QVBoxLayout;
        auto label = new QLabel("Main Content Area", centralWidget);
        layout->addWidget(label);
        centralWidget->setLayout(layout);
        setCentralWidget(centralWidget);

        // Create menu bar
        auto menuBar = new QMenuBar;
        auto fileMenu = new QMenu("File", menuBar);
        auto helloAction = new QAction("Hello button", fileMenu);

        fileMenu->addAction(helloAction);
        menuBar->addMenu(fileMenu);
        setMenuBar(menuBar);

        // Connect action
        connect(helloAction, &QAction::triggered, this, []() {
            qDebug("Button tapped");
        });

        // Create a dock widget for the drawer
        auto dockWidget = new QDockWidget("Sidebar Header", this);
        auto dockContent = new QWidget;
        auto dockLayout = new QVBoxLayout;
        dockLayout->addWidget(new QLabel("Sidebar Header", dockContent));
        dockContent->setLayout(dockLayout);
        dockWidget->setWidget(dockContent);
        addDockWidget(Qt::LeftDockWidgetArea, dockWidget);
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    MainWindow window;
    window.setWindowTitle("Subjects");
    window.show();

    return app.exec();
}
