import scrapy
from scrapy.crawler import CrawlerProcess as cp
from helpers import save_as_json as sj

class Predict_Match_spider(scrapy.Spider):
	name = "matches_spider"

	def start_requests(self):
		#download the page
		#and send it to self.parse

		yield scrapy.Request(url="https://m.forebet.com/en/football-tips-and-predictions-for-today",
			callback = self.parse)

	def parse(self,response):
		"""Scrape matches predictions"""

		#details section
		details_section = response.xpath('//*[@id="body-wrapper"]/div[2]/div[2]/div[7]/div[1]')

		home_team = details_section.xpath('//div[2]/div/a/span[1]/span/text()').get()
		away_team = details_section.xpath('//div[2]/div/a/span[2]/span/text()').get()
		start_date = details_section.xpath('/div[2]/div/a/time/span/text()').get()
		
		#probability of team wining 
		prob1 = details_section.xpath('//div[3]/span[1]/text()').get()
		probX = details_section.xpath('//div[3]/span[2]/text()').get()
		prob2 = details_section.xpath('//div[3]/span[3]/text()').get()
		
		#prediction (actual win)
		actual_win = details_section.xpath('//div[4]/span[1]/span/text()').get()
		correct_score = details_section.xpath('//div[5]/text()').get()
		average_score = details_section.xpath('//div[6]/text()').get()
		odds = details_section.xpath('//div[8]/span/text()').get()


		#live events
		#only works when page loads up
		#so user has to refresh the page
		#to see actual live event 
		#like time played, odds and scores
		time_played = details_section.xpath('//div[9]/div/div/span/text()').get()
		current_scores = details_section.xpath('//div[10]/span[1]/b/text()').get()
		live_odds = details_section.xpath('//div[11]/text()').get()

		results = {
		"home_team" : home_team,
		"away_team" : away_team,
		"start_date" : start_date,
		"probability" : {"1" : prob1, "X" : probX, "2" : prob2},
		"actual_win" : actual_win,
		"correct_score" : correct_score,
		"average_score" : average_score,
		"odds" : odds,
		"time_played" : time_played,
		"current_scores" : current_scores,
		"live_odds" : live_odds,
		}

		sj(results,'results')
		yield results


if __name__ == "__main__":
	process = cp()
	process.crawl(Predict_Match_spider)
	process.start()

