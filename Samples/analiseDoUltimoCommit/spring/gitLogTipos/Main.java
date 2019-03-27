//package com.company;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {

        String project;
        gitLog git;

        String caminhoNome="/home/gabriel/Documentos/ic/Frameworks/analiseDoUltimoCommit/spring/repositorios/springsamples.txt"; // arquivo com o nome dos projetos
        String caminhoGitlog="/home/gabriel/Documentos/ic/Frameworks/analiseDoUltimoCommit/spring/repositorios"; //caminho onde estão os log dos projetos


        BufferedReader apiName = null;
        File arq = new File(caminhoNome); //springsamples googlesamples
        apiName = new BufferedReader(new FileReader(arq));


        //aux.print();
        System.out.println("nameProject,total,add,modify,delete,tipoDistinct,java," +
                "javaDistinct,properties,jar,jarDistinct,build.gradle,buildDistinct,pom.xml,pomDistinct," +
                "manifest.xml,manifestDistinct,xml,xmlDistinct,bat," +
                "batDistinct,md,adoc,read,yaml,yamlDistinct,txt,txtDistinct,sh,shDistinct," +
                "travisyml,yml,ymlDistinct,cmd,cmdDistinct,kt,ktDistinct,json,jsonDistinct,other"); // name metrics
                //"html,json,other"); // name metrics

        while ((project = apiName.readLine()) != null)  //o nome do arquivo com git log de cada arquivo de cada projeto
        {
            String[] nome=project.split(", ");

            git = new gitLog(nome[0],caminhoGitlog);

            System.out.println(git.info());
            //System.out.println(git.getTipo());
            //git.zerar();
        }

    }
}
