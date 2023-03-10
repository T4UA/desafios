#include <stdio.h>

int main(){
    int cod_cidade, num_veiculos_passeio, num_acidentes_vitimas, soma, maior, menor, cid_max_indice, cid_min_indice, soma_vitimas, cont, i;
    float media, media_acidentes;
    char continuar;
    do{
        printf("Digite o codigo da cidade: ");
        scanf("%d", &cod_cidade);
	printf("Digite a quantidade de veiculos de passeio: ");
	scanf("%d", &num_veiculos_passeio);
	printf("Digite a quantidade de acidentes com vitimas: ");
	scanf("%d", &num_acidentes_vitimas);
	soma += num_veiculos_passeio;
	
	if(maior == 0){
	        maior = num_veiculos_passeio;
        	menor = num_veiculos_passeio;
        	cid_max_indice = cod_cidade;
        	cid_min_indice = cod_cidade;
	}else if(num_veiculos_passeio > maior){
        	maior = num_veiculos_passeio;
        	cid_max_indice = cod_cidade;
	}else if(num_veiculos_passeio < menor){
        	menor = num_veiculos_passeio;
        	cid_min_indice = cod_cidade;
	}


	if(num_veiculos_passeio < 2000){
        	soma_vitimas += num_acidentes_vitimas;
        	cont +=1;
	}

	i++;
	printf("Deseja continuar o cadastro? s ou n: ");
	scanf("%s", &continuar);
    } while(continuar == 's');

	media_acidentes = soma_vitimas / cont;
	media = soma / i;

	printf("indice_max %d - cidade %d | indice_min %d - cidade %d\n", maior, cid_max_indice, menor, cid_min_indice);
	printf("A media de veiculos nas cidades é de %.0f veiculos\n", media);
	printf("A media de acidentes de transito nas cidades com menos de 2000 veiculos é de %.0f acidentes\n", media_acidentes);
    return 0;

}
