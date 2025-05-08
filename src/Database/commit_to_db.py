from Database.models import BD_Acomodacao
from sqlalchemy.orm import Session

def commit_data_on_db(apto,db:Session):
    for item in apto:
        registros = BD_Acomodacao(
                id_acc = item['id'],
                nome_acomodacao=item['nome'],
                zona=item['zona'],
                id_proprietario = item['id_proprietario'],
                status = item['status'],
                tamanho=item['tamanho'],
                cama=item['camas'],
                qtde_quartos=item['qtde_quartos'],
                qtde_banheiros=item['qtde_banheiros'],
                cod_pais=item['codigo_pais'],
                cidade=item['cidade'],
                endereco=item['endereco'],
                bairro=item['bairro'],
                latitude=item['latitude'],
                longitude=item['longitude'],
                capacidade=item['capacidade']
        )
        db.merge(registros)
    db.commit()
    print("Dados inseridos com sucesso!")