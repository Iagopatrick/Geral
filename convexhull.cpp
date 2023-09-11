/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct Point{
    ll x, y, id;
};

Point p0;

void swap(Point &A, Point &B){ //Troca o ponteiro A com o B
    Point aux;
    aux = A;
    A = B;
    B = aux;
    
}

Point nextToTop(stack<Point> &S){//Pego o próximo ponto depois do topo
    Point temp = S.top();
    S.pop();
    Point res = S.top();
    S.push(temp);
    return res;
}

ll distSqr(Point A, Point B){//Distância ao Quadrado entre dois pontos
    return (A.x - B.x)*(A.x - B.x) + (A.y - B.y)*(A.y - B.y);
}


ll orientation(Point A, Point B, Point C){
    //Retorna a orientação dos pontos em que colineares -> 0 / horário -> 1 / Anti-Horário -> 2
    ll val = (B.y - A.y) * (C.x - B.x) - (B.x - A.x) * (C.y - B.y);
    if(val == 0) return 0;
    return (val > 0)? 1:2;
}


int compare(const void *vp1, const void *vp2){//Função para comparar o na ordenação do qsort()
    Point *p1 = (Point *) vp1;
    Point *p2 = (Point *) vp2;
    
    int o = orientation(p0, *p1, *p2);
    if(o == 0) return (distSqr(p0, *p2) >= distSqr(p0, *p1))? -1 : 1; // se sim, p2 > p1
    
    return (o == 2)? -1:1; //é Anti-Horário? se sim p2 > p1 
}

void convexHull(Point points[], ll n){
    //primeiro passo é achar o ponto mais embaixo possível - bottonmost point
    ll ymin = points[0].y, min = 0, y;
    for(ll i = 0; i < n; i++){
        y = points[i].y;
        if((y < ymin)||(y == ymin && points[i].x < points[min].x)){
            ymin = points[i].y;
            min = i;
        }
    }
    //Colocando o ponto mais embaixo na primeira posição do vetor
    swap(points[0], points[min]);
    
    p0 = points[0]; //ponto global
    
    /*  Ordena os n-1 pontos de acordo com o primeiro.
        O ponto p1 vem primeiro que o p2 na ordenação se
        p2 tiver um angulo polar (na direação Anti-Horária)
        maior que p1 */
    qsort(&points[1], n-1, sizeof(Point), compare);
    
    //Caso os angulos sejam iguais, é preciso pegar o ponto mais distante possivel, logo:
    
    ll m = 1;
    for(ll i = 1; i < n; i++){
        while(i < n - 1 && orientation(p0, points[i], points[i+1]) == 0) i++;
        points[m] = points[i];
        m++;
    }
    
    if(m < 3) return; //Caso tenha menos de 3 pontos, não é possível fazeru o menor polígono (Triângulo)
    
    //Agora é o ultimo passo, criar uma pilha que vai pegar 3 pontos e vai fazendo o fecho convexo;
    stack<Point> s;
    s.push(points[0]);
    s.push(points[1]);
    s.push(points[2]);
    
    // Process remaining n-3 points
    for (ll i = 3; i < m; i++){
       //Como ja tenho os primeiros 3 pontos dentro do vetor, agora preciso tirar
       //Aqueles que não fazem um angulo virando a esquerda, se não não fecha a figura
       //estou comparando os pontos depois do topo, topo e ponto[i]
    
        while (s.size()>1 && orientation(nextToTop(s), s.top(), points[i]) != 2){
            s.pop();
            s.push(points[i]);
            
        }
    }

   // Now stack has the output points, print contents of stack Agora vou printando os pontos
    priority_queue<Point> f;
    while (!s.empty()){
        Point p = s.top();
        cout << p.x << ", " << p.y << endl;
        
        s.pop();
    }
   
    
}







int main()
{
    Point points[] = {{0, 3}, {1, 1}, {2, 2}, {4, 4},
                    {0, 0}, {1, 2}, {3, 1}, {3, 3}};
    int n = sizeof(points)/sizeof(points[0]);
    convexHull(points, n);
    return 0;
    /*ll n, a, b;
    cin >> n;
    Point points[n];
    for(ll i = 0; i < n; i++){
        cin >> a >> b;
        points[i].x = a;
        points[i].y = b;
        points[i].id = i + 1;

    }
    convexHull(points, n);


    return 0;*/

}
