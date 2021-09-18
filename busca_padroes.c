
int main()
{
    // recebo o numero de casos de teste (string)
    char resultados[1024];
    int casos; 
    scanf("%d", &casos);
    // resultados = []
    if (casos == 0) {
        exit();
    }
    else {   
        int consultas_totais = 0;
        for (int i = 0; i < casos; i++){
            char string[100000];
            // recebo a primeira string referente ao numero de casos de teste
            scanf("%s", string);
            int m = strlen(string);
            //recebo num consultas (padroes)
            int consultas;
            scanf("%d", consultas);
            for (int j = 0; j < consultas; j++){
                consultas_totais++;
                char padrao[1000];
                scanf("%s", padrao);
                int n = strlen(padrao);
                if (m >= n){
                    // checa todas as posicoes onde o padrao pode ocorrer
                    for (int x = 0; x < (m-n+1); x++){
                        int y = 0;
                        // comparo cada caracter do padrao com do texto
                        while ( y < n){
                            if (string[x + y] != padrao[y]){
                                break;
                            }
                            y++;
                        }
                        if (y == n){
                            resultados[consultas_totais] = 's';
                            break;
                        }
                        else if ( x == (m-n) && y < n){
                            resultados[consultas_totais] = 'n';
                        }
                        
                    }
                }
                else{
                    resultados[consultas_totais] = 'n';
                }
            }

        }
        for (int i = 0; i <= consultas_totais; i++){
            print("%d \n", resultados[i]);
        }
    } 
    
};