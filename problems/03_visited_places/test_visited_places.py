import unittest
from unittest.mock import patch, call

from .visited_places import collect_places, display_places, INVALID_ENTRY_MESSAGE


class CollectingVisitedPlaces(unittest.TestCase):
    def test_ends_on_empty_line(self):
        self.patched_input_stdin.side_effect = [""]

        places = collect_places()

        self.assertEqual(0, len(places))

    def test_splits_places_description_by_coma(self):
        self.patched_input_stdin.side_effect = ["roma,italy", ""]

        places = collect_places()

        self.assertIn("italy", places)

    def test_stores_all_information_in_lower_case(self):
        self.patched_input_stdin.side_effect = ["Dijon,France", "DiJon,FrAnCe", "dijon,fRANCE", ""]

        places = collect_places()

        self.assertIn("france", places)
        self.assertEqual(1, len(places))

    def test_ignores_empty_spaces_around_country_and_city(self):
        self.patched_input_stdin.side_effect = ["   konstanz  ,    germany   ", ""]

        places = collect_places()

        self.assertIn("germany", places)

    @patch('builtins.print')
    def test_displays_an_error_message_on_an_invalid_entry(self, patched_print):
        self.patched_input_stdin.side_effect = ["beijing", ""]
        collect_places()
        patched_print.assert_called_once_with(INVALID_ENTRY_MESSAGE)

        patched_print.reset_mock()
        self.patched_input_stdin.side_effect = ["beijing;China", ""]
        collect_places()
        patched_print.assert_called_once_with(INVALID_ENTRY_MESSAGE)

        patched_print.reset_mock()
        self.patched_input_stdin.side_effect = ["Beijing,", ""]
        collect_places()
        patched_print.assert_called_once_with(INVALID_ENTRY_MESSAGE)

    def setUp(self) -> None:
        patch_input = patch('builtins.input')
        self.patched_input_stdin = patch_input.start()
        self.addCleanup(patch_input.stop)


class DisplayingVisitedPlaces(unittest.TestCase):
    def test_capitalizes_names(self):
        collected_places = self.__init_places(["roma,italy"])

        display_places(collected_places)

        self.patched_print.assert_has_calls([call("Italy"), call("\tRoma")])

    def test_prints_countries_in_alphabetical_order(self):
        collected_places = self.__init_places(["roma,italy", "beijing,China", "Dijon,France"])

        display_places(collected_places)

        self.assertEqual(call("China"), self.patched_print.mock_calls[0])
        self.assertEqual(call("France"), self.patched_print.mock_calls[2])
        self.assertEqual(call("Italy"), self.patched_print.mock_calls[4])

    def test_groups_cities_from_same_country_in_alphabetical_order(self):
        collected_places = self.__init_places(["roma,italy", "Pompei,italy", "Dijon,France", "Angers,France"])

        display_places(collected_places)

        self.patched_print.assert_has_calls([
            call("France"),
            call("\tAngers"), call("\tDijon"),
            call("Italy"),
            call("\tPompei"), call("\tRoma")
        ])

    def test_displays_number_of_visits_if_city_was_visited_multiple_times(self):
        collected_places = self.__init_places(["Konstanz,Germany"] * 3)

        display_places(collected_places)

        self.patched_print.assert_has_calls([
            call("Germany"),
            call("\tKonstanz (3)")
        ])

    def setUp(self) -> None:
        patch_print = patch('builtins.print')
        self.patched_print = patch_print.start()
        self.addCleanup(patch_print.stop)

    @staticmethod
    def __init_places(list_of_locations):
        with patch('builtins.input', side_effect=list_of_locations + [""]):
            return collect_places()


if __name__ == '__main__':
    unittest.main()
