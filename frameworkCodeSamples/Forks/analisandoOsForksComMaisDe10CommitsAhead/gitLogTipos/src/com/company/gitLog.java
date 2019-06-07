//package com.company;

import java.io.*;
import java.util.HashSet;
import java.util.Set;

public class gitLog {

    String pasta="";

    Set<String> tipo = new HashSet<>();

    Set<String> javaFiles = new HashSet<>();
    Set<String> ymlFiles = new HashSet<>();
    Set<String> jarFiles = new HashSet<>();
    Set<String> xmlFiles = new HashSet<>();
    Set<String> batFiles = new HashSet<>();
    Set<String> yamlFiles = new HashSet<>();
    Set<String> txtFiles = new HashSet<>();
    Set<String> shFiles = new HashSet<>();

    Set<String> cmdFiles = new HashSet<>();
    Set<String> ktFiles = new HashSet<>();
    Set<String> htmlFiles = new HashSet<>();
    Set<String> jsonFiles = new HashSet<>();

    Set<String> pomFiles = new HashSet<>();
    Set<String> buildFiles = new HashSet<>();
    Set<String> manifestFiles = new HashSet<>();


    int add, delete, modify;
    private int java,properties,jar,gradle,pom,xml,bat,md,adoc,yaml,txt,sh,travisyml,yml,cmd,kt,json,manifest;

    private String caminhoGitlog;


    public gitLog(String nome, String caminhoGitlog) throws IOException {
        zerar();
        setPasta(nome);
        setCaminhoLog(caminhoGitlog);
        infoArquivos();
    }

    public void setCaminhoLog(String path){
        this.caminhoGitlog = path;
    }

    public String getCaminhoLog(){
        return this.caminhoGitlog;
    }


    public void setTipo(String kind) {
        this.tipo.add(kind);
    }

    public String getPasta() {
        return pasta;
    }

    public void setPasta(String pasta) {
        this.pasta = pasta;
    }

    public Set<String> getTipo() {
        return this.tipo;
    }

    public void infoArquivos() throws IOException {

        String nomearquivo="";

        BufferedReader apiLine = null;
        File arq1 = new File(getCaminhoLog());
        apiLine = new BufferedReader(new FileReader( arq1 +"/"+ getPasta() + ".txt"));

        while ( (nomearquivo = apiLine.readLine()) != null) {

            //String[] files = nomearquivo.split("/");

            if( nomearquivo.matches("^A\t(.)*")){
                add++;
                verificarExtensao(nomearquivo);
            }
            if( nomearquivo.matches("^D\t(.)*")){
                delete++;
                verificarExtensao(nomearquivo);
            }
            if( nomearquivo.matches("^M\t(.)*")){
                modify++;
                verificarExtensao(nomearquivo);
            }
        }

    }

    public void zerar() {

        modify=0;
        delete=0;
        add=0;

        java=0;
        properties=0;
        jar=0;
        gradle=0;
        pom=0;
        xml=0;
        bat=0;
        md=0;
        adoc=0;
        yaml=0;
        txt=0;
        sh=0;
        travisyml=0;
        yml=0;
        cmd=0;
        kt=0;
        json=0;
        manifest=0;

        tipo.clear();

        javaFiles.clear();
        ymlFiles.clear();
        jarFiles.clear();
        xmlFiles.clear();
        batFiles.clear();
        yamlFiles.clear();
        txtFiles.clear();
        shFiles.clear();

        cmdFiles.clear();
        ktFiles.clear();
        htmlFiles.clear();
        jsonFiles.clear();

    }

    private void verificarExtensao(String nome) {

        if (nome.contains(".")){

            //System.out.println(nome);

            verificarTipo(nome);

            String[] formato = nome.split("[.]");
            setTipo(formato[formato.length-1]);
        }

    }

    private void verificarTipo(String nome) {

        String[] formato = nome.split("\t");

        if(formato[1].matches(".*[.]java$")) {
            java = java + 1;
            javaFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]properties$")) {
            properties = properties + 1;
        }

        if(formato[1].matches(".*[.]jar$")) {
            jar = jar + 1;
            jarFiles.add(formato[1]);
        }

        if(formato[1].matches(".*build[.]gradle$")) {
            //System.out.println(formato[1]);
            gradle = gradle + 1;
            buildFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]xml$")) {
            

        	if (formato[1].matches(".*[/]pom.xml") || formato[1].equals("pom.xml")) {
                pom = pom + 1;
                pomFiles.add(formato[1]);       		
        	}
        	else if (formato[1].matches(".*[/]AndroidManifest.xml")){
                manifest=manifest+1;
                manifestFiles.add(formato[1]);

        	}

            xmlFiles.add(formato[1]);
        	xml = xml + 1; // não pom ou manifest

        }

        if(formato[1].matches(".*[.]bat$")) {
            bat = bat + 1;
            batFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]md$")) {
            md = md + 1;
        }

        if(formato[1].matches(".*[.]adoc$")) {
            adoc = adoc + 1;
        }

        if(formato[1].matches(".*[.]yaml$")) {
            yaml = yaml + 1;
            yamlFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]txt$")) {
            txt = txt + 1;
            txtFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]sh$")) {
            sh = sh + 1;
            shFiles.add(nome);
        }

        if(formato[1].matches(".*[.]yml$")) {
            if (formato[1].contains("travis"))
                travisyml = travisyml + 1;
            else {
                yml = yml + 1;
                ymlFiles.add(formato[1]);
            }
        }

        if(formato[1].matches(".*[.]cmd$")) {
            cmd = cmd + 1;
            cmdFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]kt$")) {
            kt = kt + 1;
            ktFiles.add(formato[1]);
        }

        if(formato[1].matches(".*[.]json$")) {
            json = json + 1;
            jsonFiles.add(formato[1]);
        }
    }

    public String info(){

        int total = this.add + this.modify + this.delete;
        int read = md + adoc;

        int aux = java + properties + jar + gradle + xml + bat + md + adoc + yaml + txt + sh + yml + cmd + kt + json;

        return  getPasta() + ","+ total + "," + this.add + "," + this.modify + "," + this.delete + "," + tipo.size() + ","+
                this.java + "," + javaFiles.size() + "," + this.properties + "," + this.jar + "," + jarFiles.size() + "," +
                this.gradle + "," + buildFiles.size() + "," + this.pom + "," + pomFiles.size() + "," + this.manifest + "," +
                manifestFiles.size() + "," + this.xml + "," + xmlFiles.size() + "," +
                this.bat + "," + batFiles.size() + "," + this.md + "," + this.adoc + "," + read + "," +
                this.yaml + "," + yamlFiles.size() + "," + this.txt + "," + txtFiles.size() + "," +
                this.sh + "," + shFiles.size() + "," + //md,adoc,read
                this.travisyml + "," + this.yml + "," + ymlFiles.size() + "," + this.cmd + "," + cmdFiles.size() + "," +
                this.kt + "," + ktFiles.size() + "," + /*this.html + "," +*/
                this.json + "," + jsonFiles.size() + "," + (total - aux) ;
    }

}
