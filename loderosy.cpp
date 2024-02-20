//Perimetro 

#include <iostream>
#include <iomanip>

void menu(){
    int opc = 0;
    cout<<setw(60) <<right<<"Menu pincipal"<<endl;
    cout<<"Seleccione la opcion que desea "<<endl;
    cout<<"1.- Rectanglulo"<<endl;
    cout<<"2.- Cuadrado"<<endl;
    cout<<"3.- Circulo"<<endl;
    cout<<"4.- Trianguo"<<endl;
    cin>>opc;
    if(cin.fail()){
        cin.ignore();
        cout<<"El dato ingresado no es un digito, por favor intente nuevamente "<<endl;
        system("pause");
    }
    
}

using namespace std;


int main() {

    return 0;
}