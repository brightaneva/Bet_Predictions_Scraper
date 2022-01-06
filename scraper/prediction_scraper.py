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
		section2_matches = response.xpath('//div[@class="rcnt tr_1"]')

		x = response.xpath('//div[@class="schema"]/div[@class="rcnt tr_0"]')
		for y in x:
			teams = y.xpath('div[@class="tnms"]')
			prob = y.xpath('div[@class="fprc"]')


			dict ={
			"home": teams.xpath('div/a/span[@class="homeTeam"]/span/text()').get(),
			"away": teams.xpath('div/a/span[@class="awayTeam"]/span/text()').get(),
			"probability_percentage" : {"1x": prob.xpath('span[@class="fpr"]/text()').get(),
			"X" : prob.xpath('span[1]/text()').get(),
			"2x" : prob.xpath('span[2]/text()').get(),
			},
			"win" : y.xpath('div[@class="predict"]/span/span/text()').get(),
			"correct_score" : y.xpath('div[@class="ex_sc tabonly"]/text()').get(),
			"average_goals" : y.xpath('div[@class="avg_sc tabonly"]/text()').get(),
			}
			yield dict
			
		#prediction (actual win)



		#live events
		#only works when page loads up
		#so user has to refresh the page
		#to see actual live event 
		#like time played, odds and scores
		

		# results = {
		# "home_team" : home_team,
		# "away_team" : away_team,
		# "start_date" : start_date,
		# "probability" : {"1" : prob1, "X" : probX, "2" : prob2},
		# "actual_win" : actual_win,
		# "correct_score" : correct_score,
		# "average_score" : average_score,
		# "odds" : odds,
		# "time_played" : time_played,
		# "current_scores" : current_scores,
		# "live_odds" : live_odds,
		# }

		# sj(results,'results')
		# yield results


if __name__ == "__main__":
	process = cp()
	process.crawl(Predict_Match_spider)
	process.start()




# team = response.xpath('//span[@class="homeTeam"]/span/text()').get()