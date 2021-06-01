# frozen_string_literal: true

require 'json'
require 'faraday'
require 'net/http'
require 'logger'

logger = Logger.new($stdout)

BASE_URL = 'https://goweather.herokuapp.com/weather/'

logger.debug("Testing #{BASE_URL}")

RSpec.describe 'when you request weather forecast from weather-api' do
  let(:response) { Faraday.get url }
  let(:response_json) { JSON.parse(response.body) }

  let(:response_keys) { %w[temperature wind description forecast] }

  before { logger.info("requesting #{url}") }

  context 'when you include real city' do
    let(:url) { "#{BASE_URL}gdansk" }

    it 'has a response status equal to 200' do
      expect(response.status).to eq 200
    end

    it 'has a response containing certain keys' do
      logger.warn('Watch out! It\'s windy out there') if response_json['wind'].to_i > 10
      expect(response_json.keys).to match_array response_keys
    end
  end

  context 'when you include city that does not exist' do
    let(:url) { "#{BASE_URL}thiscitydoesntexist" }

    it 'responses with 200 status' do
      expect(response.status).to eq 200
    end

    it 'responses with certain keys' do
      expect(response_json.keys).to match_array response_keys
    end

    it 'responses with empty temperature' do
      expect(response_json['temperature']).to be_empty
    end
  end

  context 'when you do not include any city' do
    let(:url) { BASE_URL }

    it 'responses with 404 status' do
      expect(response.status).to eq 404
    end
  end
end
