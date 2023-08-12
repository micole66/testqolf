import keyword_ranker
import decision_maker
import utils
import data_processing

DATA_PATH = "path_to_data"
RANKING_CRITERIA = "ranking_criteria"
DECISION_CRITERIA = "decision_criteria"

def main():
    # Load data
    data = utils.load_data(DATA_PATH)

    # Process data
    processed_data = data_processing.process_data(data)

    # Rank keywords
    ranked_keywords = keyword_ranker.rank_keywords(processed_data, RANKING_CRITERIA)

    # Make decision
    decision = decision_maker.make_decision(ranked_keywords, DECISION_CRITERIA)

    # Save decision
    utils.save_data(decision, DATA_PATH)

if __name__ == "__main__":
    main()