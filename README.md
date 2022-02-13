# Pesatura dinamica
> Identificazione del peso tramite algoritmi di Machine Learning

L'individuazione del peso in maniera dinamica è un'applicazione attuabile in qualsiasi linea produttiva. Esso consente non solo di aumentare i ritmi produttivi evitando tempi morti, ma anche avere un costante controllo sulla massa dei pezzi prodotti. Scopo di questo progetto è lo sviluppo di un sistema predittivo per il calcolo del peso mediante tecniche di Machine Learning. A partire dai dati della cella di carico tramite un regressore lineare è possibile stimare il peso sul nastro trasportatore. 

![MisureIndustriali.png](README_images/MisureIndustriali.png)



## Tabella dei contenuti


- [Pesatura dinamica](#pesatura-dinamica)
  - [Tabella dei contenuti](#tabella-dei-contenuti)
  - [Strumentazione](#strumentazione)
  - [Taratura-Acquisizione](#taratura-acquisizione)
  - [Pre-Procesing ed estrazione features](#pre-procesing-ed-estrazione-features)
  - [Stima del peso tramite regressore Lineare](#stima-del-peso-tramite-regressore-lineare)
- [Componenti del gruppo](#componenti-del-gruppo)


## Strumentazione
La strumentazione utilizzata è la seguente:
- **Nastro trasportatore** del Laboratorio MMTLab;
- **Fotocellule:** Sick GL6
- **Schede di acquisizione** NI DAQ;
- **Cella di carico** HBM PW22C3 con fondo scala di *10 kg*

> I datasheet del seguente hardaware è presente nella seguente <a href="https://github.com/EdoGitMira/Gruppo_H_pesatura_dinamica/tree/main/datasheet" target="_blank">**cartella**</a> all'interno della repository.

## Taratura-Acquisizione

## Pre-Procesing ed estrazione features

## Stima del peso tramite regressore Lineare
Lo sviluppo dell’algoritmo di identificazione del peso`e statoeffettuato tramite regressore lineare implementato con l’utilizzodel pacchetto *scikit-learn*. La  regressione è  stata  effettuata  partendo  dal  segnale  pre-processato e calcolando poi il valore del peso in V/V. 

Questa scelta è stata effettuata per generare una regressione che sia il più possibile robusta nei confronti dei disturbi esterni. Il regressore lineare sar`a quindi del tipo:

![](https://latex.codecogs.com/svg.latex?\Large&space;y=\beta_0+\beta_1x_1+\beta_2x_2+...+\beta_nx_n) 

dove ![](https://latex.codecogs.com/svg.latex?&space;y) rappresenta il peso predetto (in V/V), ![](https://latex.codecogs.com/svg.latex?&space;\beta_0) rappresenta l'intercetta, ![](https://latex.codecogs.com/svg.latex?&space;\beta_1,\beta_2,...,\beta_n) sono i coefficienti identificati dall'algoritmo e ![](https://latex.codecogs.com/svg.latex?&space;x_1,x_2,...,x_n) rappresentano le feature del dataset. 

> Il codice, implementato tramite Google Collab è presente nella seguente <a href="https://github.com/EdoGitMira/Gruppo_H_pesatura_dinamica/tree/main/datasheet" target="_blank">**cartella**</a> all'interno della repository.

# Componenti del gruppo
|**Gioavnni Alghisi**|**Francesco Campregher**|**Marco Milanesi** | **Edoardo Mirandola** | **Abdelghani Msaad**|
| :---: |:---:|:---:|:---:|:---:|
|g.alghisi002@studenti.unibs.it|f.campregher@studenti.unibs.it|m.milanesi004@studenti.unibs.it|e.mirandola@studenti.unibs.it|a.msaad@studenti.unibs.it|

