from typing import List, Optional

class DicionarioDeSinonimos:
    
    def __init__(self) -> None:
        self._dicionario: dict[str, List[str]] = {}
    
    def adicionar_palavra(self, palavra: str, sinonimos: List[str]) -> None:   
        palavra_chave = palavra.strip().lower()
        sinonimos_limpos = [s.strip().lower() for s in sinonimos]
    
        if palavra_chave in self._dicionario:
            todos_sinonimos = self.self._dicionario[palavra_chave] + sinonimos_limpos
            self._dicionario[palavra_chave] = list(set(todos_sinonimos))
            print(f"[Atualização] Sinônimos adicionados à palavra existente: '{palavra_chave}'")
        else:
            self._dicionario[palavra_chave] = list(set(sinonimos_limpos))
            print(f"[Sucesso] Nova palavra registrada: '{palavra_chave}")
            
    def buscar_sinonimos(self, palavra: str) -> Optional[List[str]]:
        palavra_chave = palavra.strip().lower()
        
        sinonimos = self._dicionario.get(palavra_chave)
        
        if sinonimos:
            print(f"[Busca] Sinônimos de '{palavra_chave}': {','.join(sinonimos)}")
            return sinonimos
        else:
            print(f"[Aviso] A palavra '{palavra_chave}' não foi encontrada.")
            return None
        
    def remover_palavra(self, palavra: str) -> bool:
        palavra_chave = palavra.strip().lower()
        if palavra_chave in self._dicionario:
            del self._dicionario[palavra_chave]
            print(f"[Sucesso] Palavra '{palavra_chave}' removida do dicionário.")
            return True
        else:
            print(f"[Erro] Falha ao remover: '{palavra_chave}' não existe no dicionário.")
            return False
        
    def exibir_todos(self) -> None:
        print("\n--- Dicionário Completo ---")
        if not self._dicionario:
            print("O dicionário está vazio.")
        for palavra, sinonimos in self._dicionario.items():
            print(f"- {palavra.capitalize()}: {', '.join(sinonimos)}")
            print("----------------------\n")
        
if __name__ == "__main__":
    meu_dicionario = DicionarioDeSinonimos()
    
    meu_dicionario.adicionar_palavra("feliz", ["alegre", "contente", "satisfeito"])
    meu_dicionario.adicionar_palavra("rápido", ["veloz", "ágil", "apressado"])
    meu_dicionario.adicionar_palavra(" Feliz", ["Radiante", "Contente", "Alegre"])
    
    meu_dicionario.exibir_todos()
    
    sinonimos_feliz = meu_dicionario.buscar_sinonimos("FELIZ")
    sinonimos_triste = meu_dicionario.buscar_sinonimos("triste")
    print("\n")
    meu_dicionario.remover_palavra("rápido")
    meu_dicionario.remover_palavra("inteligente")
    
    meu_dicionario.exibir_todos()