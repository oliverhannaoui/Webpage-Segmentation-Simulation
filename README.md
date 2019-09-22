# Webpage Segmentation Simulation
Simulating vision based webpage segmentation using elements of the Block Growing computer vision algorithm and quantitative lingsuisitcs. <a href="https://d3i71xaburhd42.cloudfront.net/13c93315a70ffe9746f7857be4ee0aa2c4326803/1-Figure1-1.png">This </a> image displays an example of webpage  segmentation. Webpage segmentation is a domain of data science most commonly used in the field of information retrieval.<p>
<br>The following program uses just a small sample of text under the 'a' html tag on the homepage of the FlipKart e-commerce website. The principles of this program are implemented from <a href="https://www.researchgate.net/publication/221614096_A_Densitometric_Approach_to_Web_Page_Segmentation">this</a> research paper titled "A Densitometric Approach to Webpage Segmentation".</br>
<br>This program  simulates the algorithm from the research paper using scraped plain text from the 'a' html tag acting as the input blocks from the research paper. All calculations are derived from the paper. The program accomplishes the following:</br>
 <ul>
  <li>Scrapes plain text under 'a' tags from the FlipKart site using BeautifulSoup and Requests Python library to simulate the plain text input blocks from the paper.</li>
  <li>Calculates text density of each block using TextWrap module.</li>
  <li>Calculates slope deltas between adjacent blocks. Merges adjacent blocks to simulate merging of text blocks for segmentation. Merging of adjacent blocks occurs if the change in slope between adjacent blocks is below a predetermined threshold.</li>
  <li>Outputs nested lists of merged blocks that model the desired semantic structure of the webpage after webpage segmentation is completed.</li>
  
