package assignment4.dcat;

import java.io.IOException;
import java.io.InputStream;

import com.hp.hpl.jena.rdf.model.*;
import com.hp.hpl.jena.vocabulary.RDF;
import org.testng.annotations.Test;

import com.hp.hpl.jena.util.FileManager;


public class DCatParsingRdfTest
{
	@Test
	public void test1() throws IOException
	{
		String inputFileName = "src/main/resources/experimentData.ttl";

        String dcUrl = "http://purl.org/dc/terms/";

		// read the RDF/XML file
        Model model = FileManager.get().loadModel(inputFileName);

        ResIterator iter = model.listSubjects();
        while (iter.hasNext()) {
            Resource r = iter.nextResource();
            System.out.println(r.getURI());

            Statement s = r.getProperty(model.createProperty(dcUrl, "title"));
            if(s!=null) System.out.println(s.getString());

        }

		// write it to standard out
		model.write(System.out);
	}
}
