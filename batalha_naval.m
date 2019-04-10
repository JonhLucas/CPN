t = 1; % número de matriz de geradas
for j = 1:t  % laço principal
   m = zeros(10); % inicialização da matriz de zeros
   aux = zeros(10);
   navios = randi([1 10]); % sorteio da quantidade de navios
   for i = 1:navios % laço secundário, responsável por escrever cada navio.
     tipo = randi([1 2]); % sorteio do tipo. 1 para navio com tamanho 2 e 3 para tamanho 3.
     orientacao = randi([1 2]); % sorteio da horientação, 1 para vertical e 2 para horizontal
         if(orientacao == 1) % filtro para o tipo 1
             x = randi([1 8]); % sorteio da linha. Até 8 para utrapassar os limites da matriz
             y = randi([1 10]); % sorteio da coluna
             while(m(x,y) ~= 0) % laço para atualizar a posição caso esteja ocupada
               x = randi([1 8]); % nova linha 
               y = randi([1 10]); % nova coluna
             end
            if((tipo == 1) && (m(x+1, y) == 0)) % verificação das disponibilidade da posição vizinha, já que o tipo tem 1 tamanho dois e a primeira posição já foi checada
            m(x, y) = 1; % atribuição para primeira posição
            m(x+1, y) = 1; % atribuição para segunda posição 
            aux(x,y) = 1;
            aux(x+1,y) = 2;
           elseif((tipo == 2) && (m(x+2, y) == 0) && (m(x+1, y) == 0)) % verificação das disponibilidade das posições vizinhas para o tipo dois, já que o tipo tem 2 tamanho 3, a duas posições seguintes devem ser checadas
            m(x, y) = 1; % atribuição para primeira posição
            m(x+1, y) = 1; % atribuição para segunda posição
            m(x+2, y) = 1; % atribuição para segunda posição
            aux(x,y) = 1;
            aux(x+1,y) = 2;
            aux(x+2,y) = 3;
           end
         else  
             x = randi([1 10]); %tipo 2. sorteio linha
             y = randi([1 8]); % sorteio coluna.
             while(m(x,y) ~= 0) % atualização da posição, analoga a anterior
               x = randi([1 10]);
               y = randi([1 8]); 
             end
            if((tipo == 1) && (m(x, y+1) == 0)) % checagem e atribuição, analoga a anterior, só que agora nas coluna
            m(x, y) = 1;
            m(x, y+1) = 1;
            aux(x, y) = 4;
            aux(x, y+1) = 5;
           elseif((tipo == 2) && (m(x, y+2) == 0) && (m(x, y+1) == 0)) % checagem e atribuição, analoga a anterior, só que agora nas coluna
            m(x, y) = 1;
            m(x, y+1) = 1;
            m(x, y+2) = 1;
            aux(x, y) = 4;
            aux(x, y+1) = 5;
            aux(x, y+2) = 6;
           end
         end
   end
end
ocupados = zeros(10);
img = zeros(100,100); % fundo preto
for(i = 1 : 10) % grade cinza
  img(10*i:10*i, : ) = 1;
  img(:,10*i:10*i) = 1;
end
img(100,100) = 10;
jogadas = 8; % numero de jogadas permitadas, defina quantas quiser
m
for(i = 1 : jogadas)
    l = input('informe a linha desejada:');
    c = input('informe a coluna desejada:');
    ocupados(l,c) = 1;
    if(m(l,c)==0)
      img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 2;
    else
      img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 10;
      if(aux(l,c) == 1 && ocupados(l+1,c))
          if(ocupados(l+2,c) && aux(l+2,c) ==  3)
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img(l*10+1:l*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l+1)*10+1:(l+1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          else
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img(l*10+1:l*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          end
      elseif(aux(l,c) == 2 && ocupados(l-1,c))
          if(ocupados(l+1,c) && aux(l+1,c) ==  3)
              img((l-2)*10+1:(l-2)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img(l*10+1:l*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          elseif(aux(l+1,c) ~=  3)
              img((l-2)*10+1:(l-2)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          end
      elseif(aux(l,c) == 3 && ocupados(l-1,c) && ocupados(l-2,c))
          img((l-3)*10+1:(l-3)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          img((l-2)*10+1:(l-2)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
      elseif(aux(l,c) == 6 && ocupados(l,c-1) && ocupados(l,c-2))
          img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          img((l-1)*10+1:(l-1)*10+9,(c-2)*10+1:(c-2)*10+9) = 8;
          img((l-1)*10+1:(l-1)*10+9,(c-3)*10+1:(c-3)*10+9) = 8;
      elseif(aux(l,c) == 5 && ocupados(l,c-1))
          if(ocupados(l,c+1) && aux(l,c+1) == 6)
              img((l-1)*10+1:(l-1)*10+9, c*10+1:c*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c-2)*10+1:(c-2)*10+9) = 8;
          elseif(aux(l,c+1) ~=  6)
              img((l-1)*10+1:(l-1)*10+9,(c-2)*10+1:(c-2)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
          end
      elseif(aux(l,c) == 4 && ocupados(l,c+1))
          if(ocupados(l,c+2) && aux(l,c+2) == 6)
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,c*10+1:c*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,(c+1)*10+1:(c+1)*10+9) = 8;
          elseif(aux(l,c+2) ~=  6)
              img((l-1)*10+1:(l-1)*10+9,(c-1)*10+1:(c-1)*10+9) = 8;
              img((l-1)*10+1:(l-1)*10+9,c*10+1:c*10+9) = 8;
          end
      end
    end
    aux 
    figure
    imagesc(img);
end