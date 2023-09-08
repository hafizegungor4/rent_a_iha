import React, { useEffect, useState } from 'react';
import Table from '../../components/general/Table';
import { TrashFill } from 'react-bootstrap-icons';
import ConfirmModal from '../../components/general/Modal/ConfirmModal';
import { notificationActions } from "../../store/notification/notification-slice";
import { useDispatch } from "react-redux";
import ReportModal from "./ReportModal";
import { useGetAllReportsQuery, useReportRemoveMutation } from "../../store/api/reports";

export const ReportPage = () => {
  const dispatch = useDispatch();

  const [remove, isSuccess] = useReportRemoveMutation();
  const { data: reports, isLoading } = useGetAllReportsQuery();
  

  const handleDelete = async (id) => {
    await remove(id);
    if (isSuccess) {
      dispatch(notificationActions.showMessage({
        header: "Giriş",
        message: "Başarı ile silindi...",
        variant: "success"
      }));
    } else {
      dispatch(notificationActions.showMessage({
        header: "Hata",
        message: "Bir hata ile karşılaşıldı...",
        variant: "danger"
      }));
    }
  };

  return (
    <>
      <div>
        {reports?.results && !isLoading ? (
          <Table
            tableTitle="Rapor Listesi"
            searchable={true}
            addNewEntry={<ReportModal />}
            head={[
              { name: 'ID', sortable: 'numeric', width: 1 },
              { name: 'Member', sortable: 'alpha' },
              { name: 'İha', sortable: 'alpha' },
              { name: 'marka' },
              { name: 'model', sortable: 'alpha' },
              { name: 'is_renter',width: 1 },
              { name: 'Description', width: 1 },
            ]}
            body={reports.results.map((report) => [
                report.id,
                report.member,
                report.iha,
                report.marka,
                report.model,
                report.is_renter ? 'X' : '',
                report.description,

              <>
                <ReportModal isEdit={true} reportData={report} />
                <ConfirmModal
                  title="Rapor Silme"
                  body="Bu raporu silmek istediğinizden emin misiniz?"
                  onConfirm={() => handleDelete(report.id)}
                  btn={
                    <>
                      <TrashFill size={15} />
                      <span className="d-none d-md-block">Sil</span>
                    </>
                  }
                />
              </>,
            ])}
          />
        ) : (
          'Yükleniyor...'
        )}
      </div>
    </>
  );
};