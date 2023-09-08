import React, {useEffect, useState} from 'react';
import Table from '../../components/general/Table';
import {Button} from 'react-bootstrap';
import {TrashFill} from 'react-bootstrap-icons';
import CourseModal from './CourseModal';
import ConfirmModal from '../../components/general/Modal/ConfirmModal';
import {notificationActions} from "../../store/notification/notification-slice";
import {useDispatch} from "react-redux";
import {useCourseRemoveMutation, useGetAllCoursesQuery} from "../../store/api/courses";

export const CoursesPage = () => {
    const dispatch = useDispatch();

    const [remove, isSuccess] = useCourseRemoveMutation();
    const {data: iha, isLoading} = useGetAllCoursesQuery();

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

    console.log(iha);
    return (
        <>
            <div>
                {iha?.results && !isLoading ? (
                    <Table
                        tableTitle="İha Listesi"
                        searchable={true}
                        addNewEntry={<CourseModal/>}
                        head={[
                            {name: 'ID', sortable: 'numeric', width: 1},
                            {name: 'Kod'},
                            {name: 'Marka'},
                            {name: 'Model'},
                            {name: 'Ağırlık'},
                            {name: 'Açıklama'},
                        ]}
                        body={iha.results.map((course) => [
                            iha.id,
                            iha.code,
                            iha.marka,
                            iha.model,
                            iha.ağırlık,
                            iha.description,
                            <>
                                <CourseModal isEdit={true} data={iha}/>
                                <ConfirmModal
                                    title="İha Silme"
                                    body="Bu ihayı silmek istediğinizden emin misiniz?"
                                    onConfirm={() => handleDelete(course.id)}
                                    btn={
                                        <>
                                            <TrashFill size={15}/>
                                            <span className="d-none d-md-block">Sil</span>
                                        </>
                                    }
                                />
                            </>,
                        ])}
                    />
                ) : (
                    'Loading...'
                )}
            </div>
        </>
    );
};
