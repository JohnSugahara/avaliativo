from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()

    def query(self, cypher_query, parameters=None):
        with self.driver.session() as session:
            result = session.run(cypher_query, parameters)
            return [record for record in result]

    # Questão 01
    def questao_01(self):
        queries = {
            "query_1": "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf",
            "query_2": "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf",
            "query_3": "MATCH (c:City) RETURN c.name AS city_name",
            "query_4": "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS school_name, s.address AS address, s.number AS number"
        }
        
        return {key: self.query(query) for key, query in queries.items()}

    # Questão 02
    def questao_02(self):
        queries = {
            "query_1": "MATCH (t:Teacher) RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem",
            "query_2": "MATCH (c:City) RETURN avg(c.population) AS media_populacao",
            "query_3": "MATCH (c:City {cep: '37540-000'}) RETURN replace(c.name, 'a', 'A') AS city_name",
            "query_4": "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS caractere_nome"
        }
        
        return {key: self.query(query) for key, query in queries.items()}
