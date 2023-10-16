import pathlib
import unittest
from pprint import pprint


from patent_chart import parser
from patent_chart import generator

class TestParser(unittest.TestCase):
    package_dir = pathlib.Path(__file__).parents[1]
    patent_257_path = package_dir / 'test_data/US 6,484,257.pdf'
    patent_131_path = package_dir / 'test_data/US 7,600,131.pdf'
    patent_479_path = package_dir / 'test_data/US 5,870,479.pdf'
    patent_448_path = package_dir / 'test_data/US7069448.pdf'
    patent_449_path = package_dir / 'test_data/7069449.pdf'
    patent_application_path = package_dir / 'test_data/US20210365512A1.pdf'
    
    def test_parse_patent_from_pdf_path(self):
        text_lines = parser.parse_text_lines_from_pdf_path(self.patent_257_path)
        parsed_patent = parser.parse_patent_from_text_lines(text_lines)
        # print(parser.group_parsed_patent_by_page(parsed_patent)[23].column_1)
        # return
        self.assertEqual(
            parsed_patent.unique_id,
            parser.PatentUniqueID(
                patent_number='6484257',
                country_code='US',
                kind_code='B1',
            )
        )
        self.assertEqual(
            parsed_patent.beginning_of_specification,
            16
        )
        # claims = parser.parse_claims_from_parsed_patent(parsed_patent)
        # for claim in claims.claims:
        #     print(parser.serialize_claim(claim))
        # return
        # pprint(claims)
        self.assertEqual(
            parsed_patent.beginning_of_claims,
            parser.BeginningOfClaims(
                page_index=23,
                col_index=0,
                line_index=16,
            )
        )
        self.assertEqual(
            parsed_patent.end_of_claims,
            parser.EndOfClaims(
                page_index=23,
                col_index=1,
                line_index=74,
            )
        )

        text_lines = parser.parse_text_lines_from_pdf_path(self.patent_131_path)
        parsed_patent = parser.parse_patent_from_text_lines(text_lines)
        self.assertEqual(
            parsed_patent.unique_id,
            parser.PatentUniqueID(
                patent_number='7600131',
                country_code='US',
                kind_code='B1',
            )
        )
        self.assertEqual(
            parsed_patent.beginning_of_specification,
            12
        )
        self.assertEqual(
            parsed_patent.beginning_of_claims,
            parser.BeginningOfClaims(
                page_index=22,
                col_index=0,
                line_index=11,
            )
        )
        self.assertEqual(
            parsed_patent.end_of_claims,
            parser.EndOfClaims(
                page_index=22,
                col_index=1,
                line_index=42,
            )
        )

        text_lines = parser.parse_text_lines_from_pdf_path(self.patent_479_path)
        parsed_patent = parser.parse_patent_from_text_lines(text_lines)
        self.assertEqual(
            parsed_patent.unique_id,
            parser.PatentUniqueID(
                patent_number='5870479',
                country_code='US',
                kind_code='A',
            )
        )
        self.assertEqual(
            parsed_patent.beginning_of_specification,
            4
        )
        self.assertEqual(
            parsed_patent.beginning_of_claims,
            parser.BeginningOfClaims(
                page_index=7,
                col_index=0,
                line_index=8,
            )
        )
        self.assertEqual(
            parsed_patent.end_of_claims,
            parser.EndOfClaims(
                page_index=7,
                col_index=1,
                line_index=50,
            )
        )

        text_lines = parser.parse_text_lines_from_pdf_path(self.patent_application_path)
        parsed_patent = parser.parse_patent_from_text_lines(text_lines)
        self.assertEqual(
            parsed_patent.unique_id,
            parser.PatentUniqueID(
                patent_number='20210365512',
                country_code='US',
                kind_code='A1',
            )
        )

        self.assertEqual(
            parsed_patent.beginning_of_specification,
            15
        )
        # # TODO: doesn't work yet searching for specific prefatory language because there is none in this case. Would have to have some model to catch this one. Could count number of 'X.' bigrams on page, could use simple naive bayes model, could even just ask LLM.
        # self.assertEqual(
        #     parsed_patent.beginning_of_claims,
        #     parser.BeginningOfClaims(
        #         page_index=22,
        #         col_index=0,
        #         line_index=0,
        #     )
        # )
        # # TODO: doesn't work for this one either
        # self.assertEqual(
        #     parsed_patent.end_of_claims,
        #     parser.EndOfClaims(
        #         page_index=24,
        #         col_index=1,
        #         line_index=0,
        #     )
        # )

        # parsed_patent = parser.parse_patent_from_pdf_path(self.patent_448_path)
        # self.assertEqual(
        #     parsed_patent.unique_id,
        #     parser.PatentUniqueID(
        #         patent_number='7069448',
        #         country_code='US',
        #         kind_code='B2',
        #     )
        # )
        # self.assertEqual(
        #     parsed_patent.beginning_of_specification,
        #     4
        # )
        # self.assertEqual(
        #     parsed_patent.beginning_of_claims,
        #     parser.BeginningOfClaims(
        #         page_index=6,
        #         col_index=1,
        #         line_index=25,
        #     )
        # )
        # self.assertEqual(
        #     parsed_patent.end_of_claims,
        #     parser.EndOfClaims(
        #         page_index=7,
        #         col_index=1,
        #         line_index=0,
        #     )
        # )

        # TODO: doesnt work because each page of 449 is a figure. None of the text is selectable. Each page contains a pdfminer.six LTFigure object, which might be an embedded pdf. see comment in pdfminer.six/pdfminer/layout.py: class LTFigure(LTLayoutContainer):
        """Represents an area used by PDF Form objects.

        PDF Forms can be used to present figures or pictures by embedding yet
        another PDF document within a page. Note that LTFigure objects can appear
        recursively.
        """
        # So we might just need to recurse through LTFigure objects when we encounter them as the page contents.
        # parsed_patent = parser.parse_patent_from_pdf_path(self.patent_449_path)

        # TODO: test specific expected lines

    def test_parse_claims_from_parsed_patent(self):
        parsed_patent = parser.parse_patent_from_pdf_path(self.patent_257_path)
        claims = parser.parse_claims_from_parsed_patent(parsed_patent)
        first_claim = parser.serialize_claim(claims.claims[0])
        self.assertEqual(
            first_claim,
            "1. A software architecture for conducting a plurality of 15cryptographic sessions over a distributed computingenvironment, comprising:a registration entity or registry residing within a mamserver entity;an agent server entity communicating with said mam 20server;a client entity communicating with said main server andagent server;a plurality of distributed networked computers providinga mechanism for executing said main server entity,agent server entity, and client entity;a defined protocol for initiating secure communicationbetween the main server and agent server; over saidnetwork; anda system for providing one or more communicationsessions among the main server, agent server and cliententity for implementing a client decrypted bandwidthreconstitution which enables the recombination of individual parts of the decrypted client bandwidth among Nagents processing in parallel."
        )

        claim_elements = parser.serialize_claim_elements(claims.claims[0])
        # TODO: see 'over said network;' parsed as it's own element. Apparently can't rely on ';' separating claim elements in every case.
        self.assertEqual(
            claim_elements,
            ['1. A software architecture for conducting a plurality of 15cryptographic sessions over a distributed computingenvironment, comprising:', 'a registration entity or registry residing within a mamserver entity;', 'an agent server entity communicating with said mam 20server;', 'a client entity communicating with said main server andagent server;', 'a plurality of distributed networked computers providinga mechanism for executing said main server entity,agent server entity, and client entity;', 'a defined protocol for initiating secure communicationbetween the main server and agent server;', 'over saidnetwork;', 'anda system for providing one or more communicationsessions among the main server, agent server and cliententity for implementing a client decrypted bandwidthreconstitution which enables the recombination of individual parts of the decrypted client bandwidth among Nagents processing in parallel.']
        )

        # parsed_patent = parser.parse_patent_from_pdf_path(self.patent_448_path)
        # claims = parser.parse_claims_from_parsed_patent(parsed_patent)
        # print(claims)

    def test_serialize_specification_from_parsed_patent(self):
        parsed_patent = parser.parse_patent_from_pdf_path(self.patent_257_path)
        specification = parser.serialize_specification_from_parsed_patent(parsed_patent)

        self.assertEqual(
            specification[:13],
            ['1', 'SYSTEM AND METHOD FOR MAINTAINING', 'N NUMBER OF SIMULTANEOUS', 'CRYPTOGRAPHIC SESSIONS USING A', 'DISTRIBUTED COMPUTING', 'ENVIRONMENT', 'FIELD OF THE INVENTION', 'The field of the present invention relates generally to the', 'encryption and decryption of data conducted over a distrib', 'uted computer network. In particular, the field of the inven', 'tion relates to a software architecture for conducting a', 'plurality of cryptographic sessions managed over a distrib', 'uted computing environment.']
        )