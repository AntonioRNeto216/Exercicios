using System;
using System.Collections.Generic;

namespace C_ {
    class Program {
        static void Main() { // usado para chamar a função do exercício
        
        }

        /* 
            MigratoryBirds: https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=profile
        */
        static int migratoryBirds(List<int> arr) 
        {
            Dictionary<int,int> dicFinal = new Dictionary<int, int>(); // key: ID , value: frequency
            foreach(int conteudoPosicao in arr)
            {
                if(dicFinal.Count == 0 || !dicFinal.ContainsKey(conteudoPosicao))
                    dicFinal.Add(conteudoPosicao, 1);
                else
                    dicFinal[conteudoPosicao] += 1;
            }
            int idRetorno = 0; // precisa ter um valor inicial
            bool first = true;
            foreach(KeyValuePair<int,int> pair in dicFinal)
            {
                if(first)
                {
                    idRetorno = pair.Key;
                    first = false;
                } else
                {
                    if(dicFinal[idRetorno] == pair.Value)
                    {
                        idRetorno = idRetorno < pair.Key ? idRetorno : pair.Key;
                    } else if(dicFinal[idRetorno] < pair.Value)
                    {
                        idRetorno = pair.Key;
                    }
                }
            }
            return idRetorno;
        }
        ////

        /*
            BreakingRecords: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
        */
        static int[] breakingRecords(int[] scores) {
            int min = scores[0], max = scores[0], countMin = 0, countMax = 0;
            for(int i = 0; i < scores.Length; i++)
            {
                if(i!=0) {
                    if(scores[i] > max)
                    {
                        max = scores[i];
                        countMax++;
                    } else if(scores[i] < min)
                    {
                        min = scores[i];
                        countMin++;
                    }
                }
            }
            return new int[2] {countMax, countMin};
        }
        ////
        
    }
}
