# Webpage Segmentation Simulation
Simulating vision based webpage segmentation using elements of the Block Growing computer vision algorithm and quantitative lingsuisitcs. <a href="https://d3i71xaburhd42.cloudfront.net/13c93315a70ffe9746f7857be4ee0aa2c4326803/1-Figure1-1.png">Here</a> is an example of webpage segmentation, mostly used in web extraction, aims to accomplish<p>
<br>The following program uses just a small sample of text under 'a' html tags on the homepage of the FlipKart e-commerce website. The principles of this program are implemented from <a href="https://www.researchgate.net/publication/221614096_A_Densitometric_Approach_to_Web_Page_Segmentation">this</a> research paper titled "A Densitometric Approach to Webpage Segmentation".</br>
<br>This program aims to simulate the algorithm from the research paper using scraped text from 'a' html tags acting as the simulated blocks from the paper. All calculations are implemented from the paper. This program accomplishes the following:</br>
 <ul>
  <li>Scrapes text under 'a' tags from FlipKart site using BeautifulSoup and Requests Python library to simulate the plain text blocks.</li>
  <li>Calculates text density of each block using TextWrap module and calculations from the paper.</li>
  <li>Calculates slope deltas between adjacent blocks. Merges adjacent blocks to simulate merging of text blocks for segmentation. Merging of adjacent blocks occurs if the change in slope between adjacent blocks is below the threshold from the paper.</li>
  <li>Outputs nested lists of merged blocks that model the desired semantic structure of the webpage after implementing the algorithm.</li>
  
