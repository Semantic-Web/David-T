package assignment4.dcat;

import java.io.IOException;
import java.util.List;

import org.assignment4.dcat.ParserDCat;
import org.assignment4.dcat.jena.Catalog;
import org.assignment4.dcat.jena.Dataset;
import org.testng.annotations.Test;

import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.util.FileManager;


public class DCatParsingTtlTest
{
	@Test
	public void test1() throws IOException
	{
		String inputFileName = "src/main/resources/experimentData.ttl";

		Model model = FileManager.get().loadModel(inputFileName);

		List<Catalog> catalogs = ParserDCat.parse(model);

		for (Catalog catalog : catalogs)
		{
			System.out.println(catalog.getTitle());
			for (Dataset dataSet : catalog.getDataSet())
			{
				System.out.println(dataSet.getSubject());
			}
		}
	}
	
	@Test
	public void test2() throws IOException
	{
		String inputFileName = "src/main/resources/example2.ttl";

		Model model = FileManager.get().loadModel(inputFileName);

		List<Catalog> catalogs = ParserDCat.parse(model);

		for (Catalog catalog : catalogs)
		{
			System.out.println(catalog.getTitle());
			for (Dataset dataSet : catalog.getDataSet())
			{
				System.out.println(dataSet.getSubject());
			}
		}
	}
}