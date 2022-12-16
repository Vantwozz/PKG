#include "naivealgorithm.h"
#include <cmath>

#define roundf(x) floor(x + 0.5f)

NaiveAlgorithm::NaiveAlgorithm(int x1, int y1, int x2, int y2, QWidget *parent) : QWidget(parent)
{
    double dx = ((double)x2-(double)x1);
    double dy = ((double)y2-(double)y1);
    if(dx == 0 && dy == 0){
        QPointF p;
        p.setX(0);
        p.setY(0);
        points.push_back(p);
        return;
    }
    if(abs(dx)>=abs(dy)){
        double a = dy/dx;
        double x,y;
        if(x1<=x2){
            x = x1;
            y = y1;
        }else{
            x = x2;
            y = y2;
            x2 = x1;
            y2 = y1;
        }
        while(abs(x) <= abs(x2)){
            QPointF p;
            p.setX(roundf(x));
            p.setY(roundf(y));
            points.push_back(p);
            x++;
            y = y + a;
        }
    }else{
        double a = dx/dy;double x,y;
        if(y1<=y2){
            x = x1;
            y = y1;
        }else{
            x = x2;
            y = y2;
            x2 = x1;
            y2 = y1;
        }
        while(abs(y) <= abs(y2)){
            QPointF p;
            p.setX(roundf(x));
            p.setY(roundf(y));
            points.push_back(p);
            y++;
            x = x + a;
        }
    }
}
